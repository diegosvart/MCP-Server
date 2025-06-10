# Configuración de Protección de Ramas para GitHub

## 🛡️ Configuración Recomendada para las Ramas

### Para aplicar en GitHub: Settings > Branches > Add Rule

#### Protección de la rama `main`
```
Branch name pattern: main

✅ Require a pull request before merging
  ✅ Require approvals: 1
  ✅ Dismiss stale PR approvals when new commits are pushed
  ✅ Require review from code owners (si tienes CODEOWNERS)

✅ Require status checks to pass before merging
  ✅ Require branches to be up to date before merging
  Status checks:
    - CI/CD Pipeline / test
    - CI/CD Pipeline / lint
    - CI/CD Pipeline / security

✅ Require conversation resolution before merging
✅ Require signed commits (opcional)
✅ Include administrators (recomendado)
✅ Restrict pushes that create files
```

#### Protección de la rama `development`
```
Branch name pattern: development

✅ Require a pull request before merging
  ✅ Require approvals: 1
  ✅ Dismiss stale PR approvals when new commits are pushed

✅ Require status checks to pass before merging
  ✅ Require branches to be up to date before merging
  Status checks:
    - CI/CD Pipeline / test
    - CI/CD Pipeline / lint

✅ Require conversation resolution before merging
❌ Include administrators (más flexible para desarrollo)
```

## 🔐 CODEOWNERS (Opcional)

Crear archivo `.github/CODEOWNERS`:
```
# Global owner
* @diegosvart

# Código fuente principal
/src/ @diegosvart

# Tests
/tests/ @diegosvart

# CI/CD
/.github/ @diegosvart

# Documentación
/docs/ @diegosvart
*.md @diegosvart
```

## 📋 Comandos para Configurar Protección (GitHub CLI)

Si tienes GitHub CLI instalado:

```bash
# Instalar GitHub CLI si no lo tienes
# winget install GitHub.cli

# Configurar protección para main
gh api repos/diegosvart/MCP-Server/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["CI/CD Pipeline / test","CI/CD Pipeline / lint","CI/CD Pipeline / security"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null

# Configurar protección para development
gh api repos/diegosvart/MCP-Server/branches/development/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["CI/CD Pipeline / test","CI/CD Pipeline / lint"]}' \
  --field enforce_admins=false \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

## 🚦 Flujo de Trabajo con Protección

### Desarrollo Normal
1. **Feature Branch**: `git checkout -b feature/nueva-funcionalidad`
2. **Desarrollo**: Código y tests
3. **Push**: `git push origin feature/nueva-funcionalidad`
4. **PR a development**: Crear Pull Request hacia `development`
5. **Review**: Code review y aprovación
6. **Merge**: Automático después de aprobar

### Release a Producción
1. **PR development → main**: Crear Pull Request
2. **Testing**: CI/CD completo debe pasar
3. **Review**: Review obligatorio
4. **Merge**: Solo después de aprbar y pasar todos los checks

## 🔧 Beneficios de la Protección

- ✅ **Calidad**: Solo código revisado llega a producción
- ✅ **Estabilidad**: Tests obligatorios antes de merge
- ✅ **Trazabilidad**: Historial claro de cambios
- ✅ **Colaboración**: Reviews mejoran el código
- ✅ **Seguridad**: Prevent pushes directos a main

---

**Configuración preparada para aplicar en GitHub** 🛡️  
**Fecha**: 10 de junio de 2025
