"""
Ejemplo básico de uso del servidor MCP
"""

import asyncio
from src.mcp_server.server import MCPServer


async def ejemplo_basico():
    """Ejemplo básico de configuración y uso del servidor"""
    # Crear instancia del servidor
    server = MCPServer(name="ejemplo-servidor", version="1.0.0")
    
    # Registrar herramienta personalizada
    def saludar(nombre: str) -> str:
        return f"¡Hola {nombre}! Bienvenido al servidor MCP."
    
    server.register_tool(
        "saludar",
        saludar,
        "Saluda a una persona por su nombre"
    )
    
    # Registrar recurso personalizado
    datos_usuario = {
        "usuarios_activos": 42,
        "version_sistema": "2.1.0",
        "ultima_actualizacion": "2025-06-10"
    }
    
    server.register_resource(
        "estadisticas",
        datos_usuario,
        "Estadísticas del sistema"
    )
    
    # Registrar prompt personalizado
    server.register_prompt(
        "bienvenida_completa",
        "Hola {nombre}, bienvenido a {sistema}. Tenemos {usuarios} usuarios activos.",
        "Mensaje de bienvenida completo"
    )
    
    print("Servidor configurado con:")
    print(f"- Herramientas: {list(server.tools.keys())}")
    print(f"- Recursos: {list(server.resources.keys())}")
    print(f"- Prompts: {list(server.prompts.keys())}")
    
    # El servidor se iniciaría con:
    # await server.start()


if __name__ == "__main__":
    asyncio.run(ejemplo_basico())
