# Script para configurar el repositorio GitHub
# Ejecutar después de crear el repositorio en GitHub

Write-Host "🚀 Configurando repositorio GitHub para MCP-Server..." -ForegroundColor Green

# Verificar que estamos en el directorio correcto
if (!(Test-Path "setup.py")) {
    Write-Host "❌ Error: No se encontró setup.py. Ejecuta este script desde el directorio raíz del proyecto." -ForegroundColor Red
    exit 1
}

# Agregar repositorio remoto
Write-Host "📡 Agregando repositorio remoto..." -ForegroundColor Yellow
git remote add origin https://github.com/diegosvart/MCP-Server.git

# Cambiar nombre de rama a main
Write-Host "🌿 Cambiando rama master a main..." -ForegroundColor Yellow
git branch -M main

# Subir código a GitHub
Write-Host "⬆️ Subiendo código a GitHub..." -ForegroundColor Yellow
git push -u origin main

Write-Host ""
Write-Host "✅ ¡Repositorio configurado exitosamente!" -ForegroundColor Green
Write-Host "🔗 URL del repositorio: https://github.com/diegosvart/MCP-Server" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Próximos pasos recomendados:" -ForegroundColor Blue
Write-Host "   1. Agregar topics: mcp, model-context-protocol, python, fastapi, machine-learning" -ForegroundColor White
Write-Host "   2. Configurar GitHub Pages en Settings > Pages" -ForegroundColor White
Write-Host "   3. Habilitar Issues y Discussions para colaboración" -ForegroundColor White
