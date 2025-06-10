# Script para gestión de ramas de desarrollo
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("main", "development", "new-feature")]
    [string]$Action
)

function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

Write-ColorOutput "🌿 MCP Server - Gestión de Ramas" "Green"
Write-ColorOutput "================================" "Green"

switch ($Action) {
    "main" {
        Write-ColorOutput "📦 Cambiando a rama principal (main)..." "Yellow"
        git checkout main
        git pull origin main
        Write-ColorOutput "✅ Ahora estás en la rama main (producción)" "Green"
    }
    
    "development" {
        Write-ColorOutput "🚧 Cambiando a rama de desarrollo..." "Yellow"
        git checkout development
        git pull origin development
        Write-ColorOutput "✅ Ahora estás en la rama development" "Green"
        Write-ColorOutput "💡 Tip: Crea feature branches desde aquí" "Cyan"
    }
    
    "new-feature" {
        Write-ColorOutput "🔧 Creando nueva rama de funcionalidad..." "Yellow"
        
        # Asegurar que estamos en development actualizado
        git checkout development
        git pull origin development
        
        # Pedir nombre de la funcionalidad
        $featureName = Read-Host "Nombre de la funcionalidad (ej: websocket-support, auth-system)"
        $branchName = "feature/$featureName"
        
        # Crear la rama
        git checkout -b $branchName
        
        Write-ColorOutput "✅ Rama '$branchName' creada exitosamente" "Green"
        Write-ColorOutput "📝 Comandos útiles:" "Cyan"
        Write-ColorOutput "   git add ." "White"
        Write-ColorOutput "   git commit -m 'feat: descripción'" "White"
        Write-ColorOutput "   git push origin $branchName" "White"
    }
}

Write-ColorOutput "" "White"
Write-ColorOutput "📋 Estado actual:" "Blue"
git status --porcelain
if ($LASTEXITCODE -eq 0) {
    $currentBranch = git branch --show-current
    Write-ColorOutput "🌿 Rama actual: $currentBranch" "Yellow"
}

Write-ColorOutput "" "White"
Write-ColorOutput "📚 Comandos disponibles:" "Blue"
Write-ColorOutput "   .\branch-manager.ps1 main          # Ir a producción" "White"
Write-ColorOutput "   .\branch-manager.ps1 development   # Ir a desarrollo" "White"
Write-ColorOutput "   .\branch-manager.ps1 new-feature   # Crear nueva funcionalidad" "White"
