"""
Módulo de prompts MCP

Contiene los templates de prompts disponibles en el servidor
"""

from typing import Dict, Any
import string


class PromptRegistry:
    """Registro de prompts disponibles"""
    
    def __init__(self):
        self.prompts = {}
    
    def register(self, name: str, template: str, description: str = "", variables: list = None):
        """Registrar un nuevo prompt"""        
        self.prompts[name] = {
            "template": template,
            "description": description,
            "variables": variables or []
        }
    
    def get_prompt(self, name: str):
        """Obtener un prompt por nombre"""
        return self.prompts.get(name)
    
    def render_prompt(self, name: str, variables: Dict[str, Any] = None):
        """Renderizar un prompt con variables"""
        prompt = self.get_prompt(name)
        if not prompt:
            return None
        
        template = prompt["template"]
        if variables is not None:
            try:
                return template.format(**variables)
            except KeyError as e:
                return f"Error: Variable faltante {e}"
        return template
    
    def list_prompts(self):
        """Listar todos los prompts"""
        return list(self.prompts.keys())


# Instancia global del registro
prompt_registry = PromptRegistry()


# Registrar prompts por defecto
prompt_registry.register(
    "greeting",
    "Hola, soy {name}. ¿En qué puedo ayudarte hoy?",
    "Saludo personalizable con nombre",
    ["name"]
)

prompt_registry.register(
    "help_request",
    """
    Parece que necesitas ayuda. Este servidor MCP ofrece:
    
    🛠️ Herramientas disponibles: {tools}
    📄 Recursos disponibles: {resources}
    💬 Prompts disponibles: {prompts}
    
    ¿Hay algo específico en lo que pueda asistirte?
    """,
    "Prompt de solicitud de ayuda con listas dinámicas",
    ["tools", "resources", "prompts"]
)

prompt_registry.register(
    "error_response",
    """
    ❌ Ha ocurrido un error: {error_message}
    
    Detalles técnicos: {error_details}
    
    Por favor, verifica tu solicitud e inténtalo nuevamente.
    """,
    "Respuesta de error con detalles",
    ["error_message", "error_details"]
)

prompt_registry.register(
    "tool_execution",
    """
    Ejecutando herramienta: {tool_name}
    Parámetros: {parameters}
    
    Resultado:
    {result}
    """,
    "Prompt para mostrar ejecución de herramientas",
    ["tool_name", "parameters", "result"]
)

prompt_registry.register(
    "resource_access",
    """
    Accediendo al recurso: {resource_name}
    Tipo: {resource_type}
    Descripción: {description}
    
    Contenido:
    {content}
    """,
    "Prompt para mostrar acceso a recursos",
    ["resource_name", "resource_type", "description", "content"]
)

prompt_registry.register(
    "server_status",
    """
    📊 Estado del Servidor MCP
    
    Nombre: {server_name}
    Versión: {version}
    Estado: {status}
    
    Capacidades:
    - Herramientas: {tools_enabled}
    - Recursos: {resources_enabled}
    - Prompts: {prompts_enabled}
    
    Estadísticas:
    - Herramientas registradas: {tools_count}
    - Recursos registrados: {resources_count}
    - Prompts registrados: {prompts_count}
    """,
    "Prompt de estado del servidor",
    ["server_name", "version", "status", "tools_enabled", "resources_enabled", 
     "prompts_enabled", "tools_count", "resources_count", "prompts_count"]
)
