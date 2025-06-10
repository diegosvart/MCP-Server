#!/usr/bin/env python3
"""
Script para iniciar el servidor MCP con las herramientas de archivos
"""

import asyncio
import sys
from mcp_server.server import MCPServer
from mcp_server.tools import tool_registry
from mcp_server.resources import resource_registry
from mcp_server.prompts import prompt_registry


async def start_enhanced_server():
    """Iniciar servidor con todas las herramientas cargadas"""
    server = MCPServer(name="mcp-server-enhanced", version="0.1.0")
    
    # Registrar todas las herramientas del registry
    for tool_name, tool_data in tool_registry.tools.items():
        server.register_tool(
            tool_name,
            tool_data["function"],
            tool_data["description"]
        )
    
    # Registrar todos los recursos
    for resource_name, resource_data in resource_registry.resources.items():
        server.register_resource(
            resource_name,
            resource_data["data"],
            resource_data["description"]
        )
    
    # Registrar todos los prompts
    for prompt_name, prompt_data in prompt_registry.prompts.items():
        server.register_prompt(
            prompt_name,
            prompt_data["template"],
            prompt_data["description"]
        )
    
    # Iniciar servidor en puerto 8001
    await server.start(host="localhost", port=8001)


if __name__ == "__main__":
    print("🚀 Iniciando servidor MCP con herramientas de archivos...")
    print("📡 El servidor estará disponible en: http://localhost:8001")
    print("🛑 Presiona Ctrl+C para detener el servidor")
    
    try:
        asyncio.run(start_enhanced_server())
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido por el usuario")
        sys.exit(0)
