param(
    [Parameter(Mandatory = $true)]
    [string]$SdkPath,
    [string]$OutputDirectory = (Join-Path (Split-Path $PSScriptRoot -Parent) 'dist')
)

$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path (Split-Path $PSScriptRoot -Parent)).Path
$sdkRoot = (Resolve-Path -LiteralPath $SdkPath).Path
$python = Join-Path $sdkRoot 'lib/py3-windows-x86_64/python.exe'
$renpy = Join-Path $sdkRoot 'renpy.py'
if (!(Test-Path -LiteralPath $python) -or !(Test-Path -LiteralPath $renpy)) {
    throw 'Informe a pasta de um SDK Ren''Py para Windows.'
}

# O checkout contém a pasta game diretamente. O distribuidor precisa de um
# projeto convencional para não confundir seus arquivos gerados em game/.
$stage = Join-Path ([System.IO.Path]::GetTempPath()) ('requirements-whisper-build-' + [guid]::NewGuid().ToString('N'))
$stageFullPath = [System.IO.Path]::GetFullPath($stage)
$stagedProject = Join-Path $stage 'project'
$oldSavePath = $env:RENPY_PATH_TO_SAVES
New-Item -ItemType Directory -Path (Join-Path $stagedProject 'game') -Force | Out-Null
try {
    $sourceFiles = @(Get-ChildItem -LiteralPath $projectRoot -Filter '*.rpy' -File)
    $sourceFiles += Get-ChildItem -LiteralPath (Join-Path $projectRoot 'scripts') -Filter '*.rpy' -File
    $sourceFiles += Get-ChildItem -LiteralPath (Join-Path $projectRoot 'images'), (Join-Path $projectRoot 'gui') -Recurse -File
    $sourceFiles += Get-Item -LiteralPath (Join-Path $projectRoot 'tl/None/common.rpym')
    foreach ($file in $sourceFiles) {
        $relativePath = $file.FullName.Substring($projectRoot.Length + 1)
        $destination = Join-Path (Join-Path $stagedProject 'game') $relativePath
        New-Item -ItemType Directory -Path (Split-Path $destination -Parent) -Force | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $destination
    }
    $env:RENPY_PATH_TO_SAVES = Join-Path $stage 'isolated-saves'
    & $python $renpy $stagedProject lint
    if ($LASTEXITCODE -ne 0) { throw 'O lint do projeto preparado falhou.' }
    $packageDirectory = Join-Path $stage 'packages'
    & $python $renpy (Join-Path $sdkRoot 'launcher') distribute $stagedProject --package win --destination $packageDirectory
    if ($LASTEXITCODE -ne 0) { throw 'A criação do pacote Windows falhou.' }
    $packages = @(Get-ChildItem -LiteralPath $packageDirectory -Filter '*-win.zip' -File)
    if ($packages.Count -ne 1) { throw 'O distribuidor não produziu exatamente um pacote Windows.' }

    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $archive = [System.IO.Compression.ZipFile]::OpenRead($packages[0].FullName)
    try {
        $entries = $archive.Entries.FullName
        if (!($entries -match '/game/script\.rpyc$') -or !($entries -match '/TheRequirementsWhisperer\.exe$')) {
            throw 'O pacote não contém o executável e o roteiro compilado esperados.'
        }
        # renpy/audio pertence ao motor, não às músicas do projeto.
        $unwanted = @($entries -match '^[^/]+/(?:game/)?(?:tests|audio|\.git|isolated-saves)/')
        if ($unwanted.Count -gt 0) {
            throw ('O pacote incluiu material fora da entrega: ' + ($unwanted -join ', '))
        }
    } finally {
        $archive.Dispose()
    }
    New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
    $packagePath = Join-Path (Resolve-Path -LiteralPath $OutputDirectory).Path $packages[0].Name
    Copy-Item -LiteralPath $packages[0].FullName -Destination $packagePath -Force
    $hash = (Get-FileHash -LiteralPath $packagePath -Algorithm SHA256).Hash.ToLowerInvariant()
    [System.IO.File]::WriteAllText($packagePath + '.sha256', $hash + ' *' + $packages[0].Name + "`n")
    Write-Output "Pacote local: $packagePath"
    Write-Output "SHA256: $hash"
} finally {
    $env:RENPY_PATH_TO_SAVES = $oldSavePath
    if ((Test-Path -LiteralPath $stage) -and (Resolve-Path -LiteralPath $stage).Path -eq $stageFullPath) {
        Remove-Item -LiteralPath $stageFullPath -Recurse -Force
    }
}
