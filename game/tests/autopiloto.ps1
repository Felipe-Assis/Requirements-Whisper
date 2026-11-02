# Roda o piloto automático (autopiloto.rpy) no modo avulso para cada rota e
# modo, um processo do jogo por vez, e resume os relatórios JSON.
# Exemplo, da raiz do projeto:
#   powershell -File game/tests/autopiloto.ps1
#   powershell -File game/tests/autopiloto.ps1 -Rotas startup -Modos primeira,aleatorio:3
#   powershell -File game/tests/autopiloto.ps1 -Mapa pular     (pula todo tempo livre)
param(
    [string[]]$Rotas = @("saude", "startup", "corporativo"),
    [string[]]$Modos = @("primeira", "ultima", "aleatorio:1", "aleatorio:2", "aleatorio:3"),
    [string]$Sdk = "C:\Program Files (x86)\renpy-8.5.3-sdk",
    [string]$Saida = "",
    [int]$TimeoutSeg = 900,
    # Estratégia do tempo livre: prioridade, ultima, aleatorio ou pular.
    # Vazio = padrão de cada modo (ver autopiloto.rpy).
    [string]$Mapa = ""
)

# "powershell -File" entrega "a,b" como um texto só.
$Rotas = @($Rotas | ForEach-Object { $_ -split "," } | Where-Object { $_ })
$Modos = @($Modos | ForEach-Object { $_ -split "," } | Where-Object { $_ })

$projeto = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
if (-not $Saida) { $Saida = Join-Path $projeto ".test-saves\autopiloto" }
New-Item -ItemType Directory -Force $Saida | Out-Null
$python = Join-Path $Sdk "lib\py3-windows-x86_64\python.exe"
$renpy = Join-Path $Sdk "renpy.py"

$linhas = @()
foreach ($rota in $Rotas) {
    foreach ($modo in $Modos) {
        $nome = "$rota-$($modo -replace ':', '')"
        if ($Mapa) { $nome = "$nome-$Mapa" }
        $json = Join-Path $Saida "$nome.json"
        $saves = Join-Path $Saida "saves-$nome"
        Remove-Item $json -ErrorAction SilentlyContinue
        $env:RW_AUTOPILOTO = "${rota}:$modo"
        $env:RW_AUTOPILOTO_RELATORIO = $json
        $env:SDL_AUDIODRIVER = "dummy"
        if ($Mapa) { $env:RW_AUTOPILOTO_MAPA = $Mapa } else { Remove-Item Env:RW_AUTOPILOTO_MAPA -ErrorAction SilentlyContinue }
        $p = Start-Process -FilePath $python -ArgumentList "`"$renpy`"", "`"$projeto`"", "--savedir", "`"$saves`"" -PassThru
        if (-not $p.WaitForExit($TimeoutSeg * 1000)) {
            Stop-Process -Id $p.Id -Force
            $linhas += "{0,-26} TIMEOUT" -f $nome
            continue
        }
        Remove-Item -Recurse -Force $saves -ErrorAction SilentlyContinue
        if (-not (Test-Path $json)) {
            $linhas += "{0,-26} SEM RELATORIO (codigo {1})" -f $nome, $p.ExitCode
            continue
        }
        $r = Get-Content $json -Raw -Encoding UTF8 | ConvertFrom-Json
        $linhas += "{0,-26} epilogo={1} final={2}/{3} registros={4} erros={5} img={6} audio={7} tempo_livre={8} mentoria={9} pistas={10} genericos={11} {12}s" -f `
            $nome, $r.chegou_epilogo, $r.final_cena, $r.final_rota, $r.resumo_registros, `
            @($r.erros).Count, (@($r.imagens_ausentes).Count + @($r.imagens_nao_encontradas).Count), `
            @($r.audios_ausentes).Count, $r.intermissoes, $r.mentoria, @($r.pistas).Count, `
            @($r.conteudo_generico).Count, $r.segundos
    }
}
Remove-Item Env:RW_AUTOPILOTO, Env:RW_AUTOPILOTO_RELATORIO, Env:RW_AUTOPILOTO_MAPA -ErrorAction SilentlyContinue
$linhas
