"""
Módulo de herramientas MCP

Contiene las implementaciones de las herramientas disponibles en el servidor
"""

from typing import Any, Dict
import json
import datetime


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


# Registrar herramientas por defecto
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
