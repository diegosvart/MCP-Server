"""
Módulo de herramientas MCP

Contiene las implementaciones de las herramientas disponibles en el servidor
"""

from typing import Any, Dict
import json
import datetime
import os
import glob
import shutil
import pathlib


class ToolRegistry:
    """Registro de herramientas disponibles"""
    
    def __init__(self):
        self.tools = {}
    
    def register(self, name: str, function: callable, description: str = "", schema: Dict = None):
        """Registrar una nueva herramienta"""
        self.tools[name] = {
            "function": function,
            "description": description,
            "schema": schema or {}
        }
    
    def get_tool(self, name: str):
        """Obtener una herramienta por nombre"""
        return self.tools.get(name)
    
    def list_tools(self):
        """Listar todas las herramientas"""
        return list(self.tools.keys())


# Instancia global del registro
tool_registry = ToolRegistry()


# ===== HERRAMIENTAS BÁSICAS =====

def echo_tool(text: str) -> str:
    """Herramienta de eco que devuelve el texto proporcionado"""
    return f"Echo: {text}"


def datetime_tool() -> str:
    """Herramienta que devuelve la fecha y hora actual"""
    return datetime.datetime.now().isoformat()


def json_formatter_tool(data: Any) -> str:
    """Herramienta que formatea datos como JSON"""
    try:
        return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Error al formatear JSON: {str(e)}"


def calculator_tool(expression: str) -> str:
    """Herramienta de calculadora simple"""
    try:
        # Solo permitir operaciones matemáticas básicas por seguridad
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            return "Error: Solo se permiten operaciones matemáticas básicas"
        
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error en cálculo: {str(e)}"


# ===== HERRAMIENTAS DE ARCHIVOS Y DIRECTORIOS =====

def list_directory_tool(path: str = ".") -> str:
    """Lista el contenido de un directorio"""
    try:
        # Convertir a path absoluto y validar
        abs_path = os.path.abspath(path)
        if not os.path.exists(abs_path):
            return f"Error: El directorio '{path}' no existe"
        
        if not os.path.isdir(abs_path):
            return f"Error: '{path}' no es un directorio"
        
        items = []
        for item in sorted(os.listdir(abs_path)):
            item_path = os.path.join(abs_path, item)
            if os.path.isdir(item_path):
                items.append(f"📁 {item}/")
            else:
                size = os.path.getsize(item_path)
                items.append(f"📄 {item} ({size} bytes)")
        
        result = f"Contenido de '{abs_path}':\n" + "\n".join(items)
        return result if items else f"El directorio '{path}' está vacío"
        
    except Exception as e:
        return f"Error al listar directorio: {str(e)}"


def read_file_tool(file_path: str, max_lines: int = 50) -> str:
    """Lee el contenido de un archivo"""
    try:
        abs_path = os.path.abspath(file_path)
        if not os.path.exists(abs_path):
            return f"Error: El archivo '{file_path}' no existe"
        
        if not os.path.isfile(abs_path):
            return f"Error: '{file_path}' no es un archivo"
        
        with open(abs_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if len(lines) > max_lines:
            content = "".join(lines[:max_lines])
            content += f"\n... (archivo truncado, mostrando {max_lines} de {len(lines)} líneas)"
        else:
            content = "".join(lines)
        
        return f"Contenido de '{file_path}':\n{content}"
        
    except Exception as e:
        return f"Error al leer archivo: {str(e)}"


def write_file_tool(file_path: str, content: str, append: bool = False) -> str:
    """Escribe contenido en un archivo"""
    try:
        abs_path = os.path.abspath(file_path)
        
        # Crear directorio padre si no existe
        parent_dir = os.path.dirname(abs_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        
        mode = 'a' if append else 'w'
        with open(abs_path, mode, encoding='utf-8') as f:
            f.write(content)
        
        action = "agregado a" if append else "escrito en"
        return f"Contenido {action} '{file_path}' exitosamente"
        
    except Exception as e:
        return f"Error al escribir archivo: {str(e)}"


def create_directory_tool(dir_path: str) -> str:
    """Crea un directorio"""
    try:
        abs_path = os.path.abspath(dir_path)
        
        if os.path.exists(abs_path):
            return f"El directorio '{dir_path}' ya existe"
        
        os.makedirs(abs_path)
        return f"Directorio '{dir_path}' creado exitosamente"
        
    except Exception as e:
        return f"Error al crear directorio: {str(e)}"


def delete_file_tool(file_path: str) -> str:
    """Elimina un archivo"""
    try:
        abs_path = os.path.abspath(file_path)
        
        if not os.path.exists(abs_path):
            return f"Error: El archivo '{file_path}' no existe"
        
        if not os.path.isfile(abs_path):
            return f"Error: '{file_path}' no es un archivo"
        
        os.remove(abs_path)
        return f"Archivo '{file_path}' eliminado exitosamente"
        
    except Exception as e:
        return f"Error al eliminar archivo: {str(e)}"


def copy_file_tool(source: str, destination: str) -> str:
    """Copia un archivo"""
    try:
        abs_source = os.path.abspath(source)
        abs_dest = os.path.abspath(destination)
        
        if not os.path.exists(abs_source):
            return f"Error: El archivo origen '{source}' no existe"
        
        if not os.path.isfile(abs_source):
            return f"Error: '{source}' no es un archivo"
        
        # Crear directorio destino si no existe
        dest_dir = os.path.dirname(abs_dest)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        shutil.copy2(abs_source, abs_dest)
        return f"Archivo copiado de '{source}' a '{destination}' exitosamente"
        
    except Exception as e:
        return f"Error al copiar archivo: {str(e)}"


def find_files_tool(pattern: str, directory: str = ".") -> str:
    """Busca archivos que coincidan con un patrón"""
    try:
        abs_dir = os.path.abspath(directory)
        
        if not os.path.exists(abs_dir):
            return f"Error: El directorio '{directory}' no existe"
        
        # Buscar archivos usando glob
        search_pattern = os.path.join(abs_dir, "**", pattern)
        matches = glob.glob(search_pattern, recursive=True)
        
        if not matches:
            return f"No se encontraron archivos que coincidan con '{pattern}' en '{directory}'"
        
        # Formatear resultados
        result_lines = [f"Archivos encontrados con patrón '{pattern}':"]
        for match in sorted(matches):
            rel_path = os.path.relpath(match, abs_dir)
            if os.path.isfile(match):
                size = os.path.getsize(match)
                result_lines.append(f"📄 {rel_path} ({size} bytes)")
            else:
                result_lines.append(f"📁 {rel_path}/")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error al buscar archivos: {str(e)}"


def get_file_info_tool(file_path: str) -> str:
    """Obtiene información detallada de un archivo"""
    try:
        abs_path = os.path.abspath(file_path)
        
        if not os.path.exists(abs_path):
            return f"Error: '{file_path}' no existe"
        
        stat = os.stat(abs_path)
        path_obj = pathlib.Path(abs_path)
        
        info = {
            "Nombre": path_obj.name,
            "Ruta absoluta": str(abs_path),
            "Tipo": "Directorio" if os.path.isdir(abs_path) else "Archivo",
            "Tamaño": f"{stat.st_size} bytes",
            "Creado": datetime.datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "Modificado": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "Accedido": datetime.datetime.fromtimestamp(stat.st_atime).isoformat(),
        }
        
        if os.path.isfile(abs_path):
            info["Extensión"] = path_obj.suffix
        
        # Formatear como texto
        result_lines = [f"Información de '{file_path}':"]
        for key, value in info.items():
            result_lines.append(f"  {key}: {value}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error al obtener información: {str(e)}"


# Registrar herramientas básicas
tool_registry.register(
    "echo",
    echo_tool,
    "Devuelve el texto proporcionado como eco",
    {"type": "function", "parameters": {"text": {"type": "string"}}}
)

tool_registry.register(
    "datetime",
    datetime_tool,
    "Obtiene la fecha y hora actual",
    {"type": "function", "parameters": {}}
)

tool_registry.register(
    "json_formatter",
    json_formatter_tool,
    "Formatea datos como JSON",
    {"type": "function", "parameters": {"data": {"type": "any"}}}
)

tool_registry.register(
    "calculator",
    calculator_tool,
    "Calculadora simple para operaciones matemáticas básicas",
    {"type": "function", "parameters": {"expression": {"type": "string"}}}
)

# Registrar herramientas de archivos y directorios
tool_registry.register(
    "list_directory",
    list_directory_tool,
    "Lista el contenido de un directorio",
    {"type": "function", "parameters": {"path": {"type": "string", "default": "."}}}
)

tool_registry.register(
    "read_file",
    read_file_tool,
    "Lee el contenido de un archivo",
    {"type": "function", "parameters": {"file_path": {"type": "string"}, "max_lines": {"type": "integer", "default": 50}}}
)

tool_registry.register(
    "write_file",
    write_file_tool,
    "Escribe contenido en un archivo",
    {"type": "function", "parameters": {"file_path": {"type": "string"}, "content": {"type": "string"}, "append": {"type": "boolean", "default": False}}}
)

tool_registry.register(
    "create_directory",
    create_directory_tool,
    "Crea un directorio",
    {"type": "function", "parameters": {"dir_path": {"type": "string"}}}
)

tool_registry.register(
    "delete_file",
    delete_file_tool,
    "Elimina un archivo",
    {"type": "function", "parameters": {"file_path": {"type": "string"}}}
)

tool_registry.register(
    "copy_file",
    copy_file_tool,
    "Copia un archivo",
    {"type": "function", "parameters": {"source": {"type": "string"}, "destination": {"type": "string"}}}
)

tool_registry.register(
    "find_files",
    find_files_tool,
    "Busca archivos que coincidan con un patrón",
    {"type": "function", "parameters": {"pattern": {"type": "string"}, "directory": {"type": "string", "default": "."}}}
)

tool_registry.register(
    "get_file_info",
    get_file_info_tool,
    "Obtiene información detallada de un archivo",
    {"type": "function", "parameters": {"file_path": {"type": "string"}}}
)
