# Gera o pacote Windows do jogo e confere o conteudo do ZIP.
# Uso (a partir de qualquer pasta):
#   powershell -ExecutionPolicy Bypass -File tools\build-windows.ps1 [-SdkPath <sdk>] [-OutputDirectory <pasta>]
# Passos: lint limpo -> distribute --package win -> ZIP tem o .exe e o roteiro
# compilado e nao tem tests/docs/tools/saves -> copia para dist/ com o SHA256.
# Texto sem acentos: o PowerShell 5.1 le .ps1 sem BOM como ANSI.
param(
    [string]$SdkPath = 'C:\Program Files (x86)\renpy-8.5.3-sdk',
    [string]$OutputDirectory = (Join-Path (Split-Path $PSScriptRoot -Parent) 'dist')
)

$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path (Split-Path $PSScriptRoot -Parent)).Path
$sdkRoot = (Resolve-Path -LiteralPath $SdkPath).Path
$python = Join-Path $sdkRoot 'lib/py3-windows-x86_64/python.exe'
$renpy = Join-Path $sdkRoot 'renpy.py'
if (!(Test-Path -LiteralPath $python) -or !(Test-Path -LiteralPath $renpy)) {
    throw 'Informe a pasta de um SDK Ren''Py para Windows (-SdkPath).'
}
if (!(Test-Path -LiteralPath (Join-Path $projectRoot 'game/script.rpy'))) {
    throw 'A raiz do projeto precisa conter game/script.rpy.'
}

# Pasta temporaria propria: saves isolados e pacotes gerados ficam fora do
# projeto e sao apagados no fim, mesmo em caso de erro.
$stage = Join-Path ([System.IO.Path]::GetTempPath()) ('requirements-whisper-build-' + [guid]::NewGuid().ToString('N'))
$stageFullPath = [System.IO.Path]::GetFullPath($stage)
$packageDirectory = Join-Path $stage 'packages'
$oldSavePath = $env:RENPY_PATH_TO_SAVES
New-Item -ItemType Directory -Path $packageDirectory -Force | Out-Null
try {
    $env:RENPY_PATH_TO_SAVES = Join-Path $stage 'isolated-saves'

    # 1. Lint. O relatorio vai para errors.txt; tudo antes de "Statistics:"
    #    alem do cabecalho e um problema.
    & $python $renpy $projectRoot lint
    if ($LASTEXITCODE -ne 0) { throw 'O lint falhou.' }
    $report = Get-Content -LiteralPath (Join-Path $projectRoot 'errors.txt') -Raw -Encoding UTF8
    $beforeStats = ($report -split 'Statistics:')[0]
    $problems = @($beforeStats -split "`r?`n" | Where-Object { $_.Trim() -and ($_ -notmatch 'lint report, generated at') })
    if ($problems.Count -gt 0) {
        throw ("O lint encontrou problemas:`n" + ($problems -join "`n"))
    }

    # 2. Pacote Windows.
    & $python $renpy (Join-Path $sdkRoot 'launcher') distribute $projectRoot --package win --destination $packageDirectory
    if ($LASTEXITCODE -ne 0) { throw 'A criacao do pacote Windows falhou.' }
    $packages = @(Get-ChildItem -LiteralPath $packageDirectory -Filter '*-win.zip' -File)
    if ($packages.Count -ne 1) { throw 'O distribuidor nao produziu exatamente um pacote Windows.' }

    # 3. Conteudo do ZIP.
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $archive = [System.IO.Compression.ZipFile]::OpenRead($packages[0].FullName)
    try {
        $entries = @($archive.Entries | ForEach-Object { $_.FullName })
        if (!($entries -match '/TheRequirementsWhisperer\.exe$')) {
            throw 'O pacote nao contem TheRequirementsWhisperer.exe.'
        }
        if (!($entries -match '/game/script\.rpyc$')) {
            throw 'O pacote nao contem o roteiro compilado (game/script.rpyc).'
        }
        # So pastas do projeto (raiz ou game/); bibliotecas do motor ficam de fora da regra.
        $unwanted = @($entries -match '^[^/]+/(?:game/)?(?:tests|docs|tools|saves|dist|\.test-saves|\.git)/')
        if ($unwanted.Count -gt 0) {
            throw ('O pacote incluiu material fora da entrega: ' + (($unwanted | Select-Object -First 20) -join ', '))
        }
    } finally {
        $archive.Dispose()
    }

    # 4. Copia para dist/ com o SHA256 ao lado.
    New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
    $packagePath = Join-Path (Resolve-Path -LiteralPath $OutputDirectory).Path $packages[0].Name
    Copy-Item -LiteralPath $packages[0].FullName -Destination $packagePath -Force
    $hash = (Get-FileHash -LiteralPath $packagePath -Algorithm SHA256).Hash.ToLowerInvariant()
    [System.IO.File]::WriteAllText($packagePath + '.sha256', $hash + ' *' + $packages[0].Name + "`n")
    Write-Output "Pacote: $packagePath"
    Write-Output "SHA256: $hash"
} finally {
    $env:RENPY_PATH_TO_SAVES = $oldSavePath
    if ((Test-Path -LiteralPath $stage) -and ((Resolve-Path -LiteralPath $stage).Path -eq $stageFullPath)) {
        Remove-Item -LiteralPath $stageFullPath -Recurse -Force
    }
}
