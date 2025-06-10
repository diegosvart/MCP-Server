"""
Servidor principal MCP

Implementa el servidor del Protocolo de Contexto de Modelo usando FastAPI
"""

import asyncio
import logging
from typing import Dict, List, Any
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class MCPServer:
    """Servidor principal MCP"""
    
    def __init__(self, name: str = "mcp-server", version: str = "0.1.0"):
        self.name = name
        self.version = version
        self.app = FastAPI(title=name, version=version)
        self.tools: Dict[str, Any] = {}
        self.resources: Dict[str, Any] = {}
        self.prompts: Dict[str, Any] = {}
        
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Configurar rutas
        self._setup_routes()
    
    def _setup_routes(self):
        """Configurar rutas de la API"""
        
        @self.app.get("/")
        async def root():
            return {
                "name": self.name,
                "version": self.version,
                "protocol": "model-context-protocol",
                "capabilities": {
                    "tools": True,
                    "resources": True,
                    "prompts": True,
                    "discovery": False,
                    "sampling": False,
                    "roots": False
                }
            }
        
        @self.app.get("/tools")
        async def list_tools():
            """Listar herramientas disponibles"""
            return {"tools": list(self.tools.keys())}
        
        @self.app.get("/resources")
        async def list_resources():
            """Listar recursos disponibles"""
            return {"resources": list(self.resources.keys())}
        
        @self.app.get("/prompts")
        async def list_prompts():
            """Listar prompts disponibles"""
            return {"prompts": list(self.prompts.keys())}
    
    def register_tool(self, name: str, function: callable, description: str = ""):
        """Registrar una herramienta"""
        self.tools[name] = {
            "function": function,
            "description": description
        }
        self.logger.info(f"Herramienta registrada: {name}")
    
    def register_resource(self, name: str, data: Any, description: str = ""):
        """Registrar un recurso"""
        self.resources[name] = {
            "data": data,
            "description": description
        }
        self.logger.info(f"Recurso registrado: {name}")
    
    def register_prompt(self, name: str, template: str, description: str = ""):
        """Registrar un prompt"""
        self.prompts[name] = {
            "template": template,
            "description": description
        }
        self.logger.info(f"Prompt registrado: {name}")
    
    async def start(self, host: str = "localhost", port: int = 8000):
        """Iniciar el servidor"""
        self.logger.info(f"Iniciando servidor MCP en {host}:{port}")
        config = uvicorn.Config(
            app=self.app,
            host=host,
            port=port,
            log_level="info"
        )
        server = uvicorn.Server(config)
        await server.serve()


def main():
    """Función principal para ejecutar el servidor"""
    server = MCPServer()
    
    # Registrar herramientas de ejemplo
    server.register_tool(
        "echo",
        lambda text: f"Echo: {text}",
        "Herramienta de eco que devuelve el texto proporcionado"
    )
    
    # Registrar recursos de ejemplo
    server.register_resource(
        "system_info",
        {"version": "0.1.0", "status": "running"},
        "Información del sistema"
    )
    
    # Registrar prompts de ejemplo
    server.register_prompt(
        "greeting",
        "Hola, soy {name}. ¿En qué puedo ayudarte hoy?",
        "Prompt de saludo personalizable"
    )
    
    # Ejecutar servidor
    asyncio.run(server.start())


if __name__ == "__main__":
    main()
