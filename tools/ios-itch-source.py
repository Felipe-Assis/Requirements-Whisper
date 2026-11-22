"""Prepare the pinned, publicly released game for an iOS rebuild."""

from hashlib import sha256
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import json
from pathlib import Path, PurePosixPath
import shutil
import stat
import sys
from tempfile import TemporaryFile
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPCookieProcessor, Request, build_opener
from zipfile import ZipFile


GAME = 'https://felipe-assis.itch.io/requirement-whisper'
VERSION = '1.8.1-epilogo'
EXPECTED = {
    'options.rpy': 'e3082b5cdef8531219b8b32dcbeae27efb787dc47566054df42f680160e091d4',
    'scripts/mechanics/epilogo_vivo.rpy': '31729aa0417d0ea053b818068f7190b922a83aacc8b3c8485790add2bf294905',
}


class DownloadPage(HTMLParser):
    csrf = ''

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'meta' and values.get('name') == 'csrf_token':
            self.csrf = values.get('content') or ''


def download(opener, target):
    latest_url = 'https://api.itch.io/wharf/latest?game_id=5371877&channel_name=windows'
    with opener.open(latest_url, timeout=60) as response:
        if json.load(response).get('latest') != VERSION:
            raise ValueError(f'The Windows channel must contain {VERSION}.')

    def post(url, fields, referer):
        request = Request(url, urlencode(fields).encode(), headers={
            'Referer': referer, 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json',
        })
        with opener.open(request, timeout=60) as response:
            return json.load(response)['url']

    page = post(f'{GAME}/download_url', {}, GAME)
    if urlsplit(page).hostname != urlsplit(GAME).hostname or urlsplit(page).scheme != 'https':
        raise ValueError('Unexpected itch.io download page.')
    parser = DownloadPage()
    with opener.open(page, timeout=60) as response:
        parser.feed(response.read().decode('utf-8'))
    package = post(f'{GAME}/file/20554972?source=game_download', {'csrf_token': parser.csrf}, page)
    if urlsplit(package).scheme != 'https':
        raise ValueError('Expected an HTTPS archive.')
    with opener.open(package, timeout=120) as response:
        shutil.copyfileobj(response, target, length=1024 * 1024)
    target.seek(0)


def extract_game(archive, destination):
    files = {}
    for entry in archive.infolist():
        parts = PurePosixPath(entry.filename).parts
        if entry.is_dir() or len(parts) < 3 or parts[1] != 'game':
            continue
        relative = PurePosixPath(*parts[2:])
        if '..' in parts or '\\' in entry.filename or parts[0] == '/':
            raise ValueError(f'Invalid archive path {entry.filename!r}.')
        if stat.S_ISLNK(entry.external_attr >> 16) or relative in files:
            raise ValueError(f'Invalid archive entry {entry.filename!r}.')
        files[relative] = entry

    for name, expected in EXPECTED.items():
        entry = files[PurePosixPath(name)]
        if sha256(archive.read(entry)).hexdigest() != expected:
            raise ValueError(f'Unexpected {VERSION} source in {name}.')

    for path, entry in files.items():
        target = destination / 'game' / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with archive.open(entry) as source, target.open('xb') as output:
            shutil.copyfileobj(source, output)
    print(f'Extracted {len(files)} verified-release game files from itch.io.', flush=True)


if __name__ == '__main__':
    destination = Path(sys.argv[1]).resolve(strict=True)
    with TemporaryFile(dir=destination) as package:
        download(build_opener(HTTPCookieProcessor(CookieJar())), package)
        with ZipFile(package) as archive:
            extract_game(archive, destination)
