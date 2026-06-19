<#
  Builds a clean Zenodo upload archive from this repository.

  EXCLUDES (must not go to a public archive):
    - references/         third-party copyrighted PDFs (private research use only)
    - .git, caches, LaTeX build artifacts, *.log, *.pyc
    - code/data/{elliptic,realgraphs,topo_tmp}  large PUBLIC datasets (not ours to redistribute)
  INCLUDES:
    - paper/ (LaTeX + figures + .bbl), code/ (with data/twins + results), README, LICENSE,
      requirements.txt, CITATION.cff, .zenodo.json

  Usage:   powershell -ExecutionPolicy Bypass -File make_zenodo_archive.ps1
  Output:  ../graph-phishing-spear-detection-zenodo-v1.0.0.zip
#>
$ErrorActionPreference = "Stop"
$src   = $PSScriptRoot
$stage = Join-Path $env:TEMP "gpsd-zenodo-stage"
$zip   = Join-Path (Split-Path $src -Parent) "graph-phishing-spear-detection-zenodo-v1.0.0.zip"

if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
if (Test-Path $zip)   { Remove-Item $zip -Force }

# robocopy exit codes 0-7 are success; treat >=8 as failure
$xd = @(
  (Join-Path $src "references"),
  (Join-Path $src ".git"),
  (Join-Path $src "code\data\elliptic"),
  (Join-Path $src "code\data\realgraphs"),
  (Join-Path $src "code\data\topo_tmp"),
  "__pycache__", ".pytest_cache", ".ipynb_checkpoints"
)
$xf = @("*.log","*.pyc","*.aux","*.out","*.synctex.gz","*.fls","*.fdb_latexmk",
        "*.toc","*.blg","SUBMISSION_CHECKLIST_CS.md","make_zenodo_archive.ps1")

robocopy "$src" "$stage" /E /NFL /NDL /NJH /NJS /NP /XD @xd /XF @xf | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed with code $LASTEXITCODE" }

Compress-Archive -Path (Join-Path $stage "*") -DestinationPath $zip -Force
Remove-Item $stage -Recurse -Force

$mb = [math]::Round((Get-Item $zip).Length / 1MB, 2)
Write-Host "OK -> $zip  ($mb MB)"
Write-Host "Verify it contains NO references/ and NO third-party PDFs before uploading to Zenodo."
