# Exit immediately if any command fails
$ErrorActionPreference = "Stop"

# Check if exactly 2 arguments are provided
if ($args.Count -ne 2) {
    Write-Host "Error: Incorrect number of arguments."
    Write-Host "Usage: .\setup.ps1 `"<project_name>`" `"<project_description>`""
    exit 1
}

$PROJECT_NAME = $args[0]
$PROJECT_DESCRIPTION = $args[1]

Write-Host "Setting up Python project: $PROJECT_NAME"
Write-Host "------------------------------------------------"

# 1. Create and activate virtual environment
Write-Host "1. Creating virtual environment with uv (Python 3.12)..."
uv venv --python 3.12
& .venv\Scripts\Activate.ps1

# 2. Create pyproject.toml
Write-Host "2. Creating pyproject.toml..."
@"
[project]
name = "$PROJECT_NAME"
version = "0.0.1"
description = "$PROJECT_DESCRIPTION"
dependencies = [
    "pandas>=3.0.2",
]
"@ | Out-File -FilePath "pyproject.toml" -Encoding utf8

# 3. Sync dependencies
Write-Host "3. Syncing dependencies..."
uv sync

# 4. Create .vscode folder
Write-Host "4. Creating .vscode directory..."
New-Item -ItemType Directory -Force -Path .vscode | Out-Null

# 5. Create launch.json
Write-Host "5. Creating launch.json..."
@"
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "$PROJECT_NAME",
            "type": "debugpy",
            "request": "launch",
            "program": "`${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "`${workspaceFolder}",
                "ROOTDIR": "`${workspaceFolder}/"
            }
        }
    ]
}
"@ | Out-File -FilePath ".vscode\launch.json" -Encoding utf8


# TODO, add gitignore

# 7. Open VS Code
Write-Host "7. Opening VS Code..."
code .

Write-Host "------------------------------------------------"
Write-Host "Setup complete! Your environment is active and VS Code is launching."