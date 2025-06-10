# Documentación del Servidor MCP

## Introducción

Este proyecto implementa un servidor del Protocolo de Contexto de Modelo (MCP) usando Python y FastAPI. El servidor proporciona una interfaz estándar para que los clientes MCP accedan a herramientas, recursos y prompts.

## Arquitectura

### Componentes Principales

1. **MCPServer**: Clase principal que implementa el servidor
2. **ToolRegistry**: Registro de herramientas disponibles
3. **ResourceRegistry**: Registro de recursos disponibles
4. **PromptRegistry**: Registro de prompts disponibles

### Estructura de Directorios

```
src/mcp_server/
├── __init__.py          # Módulo principal
├── server.py            # Implementación del servidor
├── tools/
│   └── __init__.py      # Herramientas predefinidas
├── resources/
│   └── __init__.py      # Recursos predefinidos
└── prompts/
    └── __init__.py      # Prompts predefinidos
```

## API Endpoints

### GET /
Retorna información básica del servidor y sus capacidades.

```json
{
  "name": "mcp-server",
  "version": "0.1.0",
  "protocol": "model-context-protocol",
  "capabilities": {
    "tools": true,
    "resources": true,
    "prompts": true,
    "discovery": false,
    "sampling": false,
    "roots": false
  }
}
```

### GET /tools
Lista todas las herramientas disponibles.

### GET /resources
Lista todos los recursos disponibles.

### GET /prompts
Lista todos los prompts disponibles.

## Herramientas Predefinidas

### echo
- **Descripción**: Devuelve el texto proporcionado como eco
- **Parámetros**: `text` (string)
- **Ejemplo**: `echo("Hola mundo")` → `"Echo: Hola mundo"`

### datetime
- **Descripción**: Obtiene la fecha y hora actual
- **Parámetros**: Ninguno
- **Ejemplo**: `datetime()` → `"2025-06-10T10:30:00"`

### json_formatter
- **Descripción**: Formatea datos como JSON
- **Parámetros**: `data` (any)
- **Ejemplo**: `json_formatter({"key": "value"})` → JSON formateado

### calculator
- **Descripción**: Calculadora simple para operaciones matemáticas básicas
- **Parámetros**: `expression` (string)
- **Ejemplo**: `calculator("2 + 2")` → `"4"`

## Recursos Predefinidos

### system_info
Información del sistema operativo y entorno.

### config_info
Información de configuración del servidor.

### help_text
Texto de ayuda del servidor.

## Prompts Predefinidos

### greeting
Saludo personalizable con nombre.
- **Variables**: `name`
- **Template**: `"Hola, soy {name}. ¿En qué puedo ayudarte hoy?"`

### help_request
Prompt de solicitud de ayuda con listas dinámicas.
- **Variables**: `tools`, `resources`, `prompts`

### error_response
Respuesta de error con detalles.
- **Variables**: `error_message`, `error_details`

## Uso Programático

### Crear un Servidor

```python
from mcp_server import MCPServer

server = MCPServer(name="mi-servidor", version="1.0.0")
```

### Registrar Herramienta

```python
def mi_herramienta(param: str) -> str:
    return f"Procesado: {param}"

server.register_tool(
    "mi_herramienta",
    mi_herramienta,
    "Descripción de mi herramienta"
)
```

### Registrar Recurso

```python
datos = {"clave": "valor"}
server.register_resource(
    "mi_recurso",
    datos,
    "Descripción de mi recurso"
)
```

### Registrar Prompt

```python
server.register_prompt(
    "mi_prompt",
    "Hola {nombre}, bienvenido a {sistema}",
    "Mi prompt personalizado"
)
```

### Iniciar el Servidor

```python
import asyncio

async def main():
    await server.start(host="localhost", port=8000)

asyncio.run(main())
```

## Configuración

El servidor se puede configurar mediante el archivo `config/server_config.json`:

```json
{
  "server": {
    "name": "mcp-server",
    "version": "0.1.0",
    "host": "localhost",
    "port": 8000,
    "debug": false
  },
  "capabilities": {
    "tools": true,
    "resources": true,
    "prompts": true
  }
}
```

## Testing

Ejecutar todas las pruebas:

```bash
pytest tests/
```

Ejecutar pruebas específicas:

```bash
pytest tests/test_server.py
pytest tests/test_tools.py
pytest tests/test_prompts.py
```

## Ejemplos

Ver el directorio `examples/` para ejemplos completos de uso.

## Herramientas de Archivos

El servidor incluye herramientas avanzadas para el manejo de archivos y directorios:

### list_directory
Lista el contenido de un directorio.

**Parámetros:**
- `path` (string): Ruta del directorio a listar

**Ejemplo de uso:**
```python
# Listar directorio actual
result = call_tool("list_directory", ".")
```

### read_file
Lee el contenido de un archivo.

**Parámetros:**
- `file_path` (string): Ruta del archivo a leer

**Ejemplo de uso:**
```python
content = call_tool("read_file", "documento.txt")
```

### write_file
Escribe contenido a un archivo.

**Parámetros:**
- `file_path` (string): Ruta del archivo a escribir
- `content` (string): Contenido a escribir

**Ejemplo de uso:**
```python
result = call_tool("write_file", "nuevo.txt", "Contenido del archivo")
```

### create_directory
Crea un nuevo directorio.

**Parámetros:**
- `dir_path` (string): Ruta del directorio a crear

**Ejemplo de uso:**
```python
result = call_tool("create_directory", "mi_directorio")
```

### delete_file
Elimina un archivo o directorio.

**Parámetros:**
- `file_path` (string): Ruta del archivo o directorio a eliminar

**Ejemplo de uso:**
```python
result = call_tool("delete_file", "archivo_temporal.txt")
```

### copy_file
Copia un archivo de una ubicación a otra.

**Parámetros:**
- `source_path` (string): Ruta del archivo origen
- `dest_path` (string): Ruta del archivo destino

**Ejemplo de uso:**
```python
result = call_tool("copy_file", "original.txt", "copia.txt")
```

### find_files
Busca archivos usando patrones glob.

**Parámetros:**
- `pattern` (string): Patrón de búsqueda (ej: "*.py", "docs/*.md")
- `base_path` (string, opcional): Directorio base para la búsqueda (default: ".")

**Ejemplo de uso:**
```python
# Buscar todos los archivos Python
result = call_tool("find_files", "*.py")

# Buscar archivos Markdown en docs/
result = call_tool("find_files", "*.md", "docs")
```

### get_file_info
Obtiene información detallada de un archivo.

**Parámetros:**
- `file_path` (string): Ruta del archivo

**Ejemplo de uso:**
```python
info = call_tool("get_file_info", "documento.pdf")
```

## Endpoint para Ejecutar Herramientas

### POST /tools/call
Ejecuta una herramienta específica del servidor.

**Formato de solicitud:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "nombre_herramienta",
    "arguments": ["arg1", "arg2"] // o {"param": "value"}
  }
}
```

**Formato de respuesta:**
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resultado de la herramienta"
    }
  ]
}
```

**Ejemplo con curl:**
```bash
curl -X POST http://localhost:8001/tools/call \
  -H "Content-Type: application/json" \
  -d '{
    "method": "tools/call",
    "params": {
      "name": "list_directory",
      "arguments": ["."]
    }
  }'
```
