"""
Módulo de recursos MCP

Contiene las implementaciones de los recursos disponibles en el servidor
"""

from typing import Any, Dict
import json
import os


class ResourceRegistry:
    """Registro de recursos disponibles"""
    
    def __init__(self):
        self.resources = {}
    
    def register(self, name: str, data: Any, description: str = "", resource_type: str = "data"):
        """Registrar un nuevo recurso"""
        self.resources[name] = {
            "data": data,
            "description": description,
            "type": resource_type
        }
    
    def get_resource(self, name: str):
        """Obtener un recurso por nombre"""
        return self.resources.get(name)
    
    def list_resources(self):
        """Listar todos los recursos"""
        return list(self.resources.keys())


# Instancia global del registro
resource_registry = ResourceRegistry()


def get_system_info():
    """Obtener información del sistema"""
    return {
        "platform": os.name,
        "cwd": os.getcwd(),
        "env_vars": dict(os.environ),
        "python_version": "3.x"
    }


def get_config_info():
    """Obtener información de configuración"""
    return {
        "server_name": "mcp-server",
        "version": "0.1.0",
        "capabilities": {
            "tools": True,
            "resources": True,
            "prompts": True,
            "discovery": False,
            "sampling": False,
            "roots": False
        }
    }


# Registrar recursos por defecto
resource_registry.register(
    "system_info",
    get_system_info(),
    "Información del sistema operativo y entorno",
    "system"
)

resource_registry.register(
    "config_info",
    get_config_info(),
    "Información de configuración del servidor",
    "config"
)

resource_registry.register(
    "help_text",
    {
        "title": "Ayuda del Servidor MCP",
        "content": """
        Este servidor MCP proporciona las siguientes funcionalidades:
        
        HERRAMIENTAS:
        - echo: Devuelve el texto proporcionado
        - datetime: Obtiene la fecha y hora actual
        - json_formatter: Formatea datos como JSON
        - calculator: Calculadora simple
        
        RECURSOS:
        - system_info: Información del sistema
        - config_info: Configuración del servidor
        - help_text: Este texto de ayuda
        
        PROMPTS:
        - greeting: Saludo personalizable
        - help_request: Solicitud de ayuda
        - error_response: Respuesta de error
        """
    },
    "Texto de ayuda del servidor",
    "documentation"
)
