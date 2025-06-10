#!/usr/bin/env python3
"""
Script de inicio para el servidor MCP
"""

import os
import sys
import json
import argparse
import asyncio
from pathlib import Path

# Agregar el directorio src al path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))

from mcp_server.server import MCPServer


def cargar_configuracion(config_path: str = None):
    """Cargar configuración desde archivo JSON"""
    if config_path is None:
        config_path = current_dir / "config" / "server_config.json"
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Archivo de configuración no encontrado: {config_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error al leer configuración: {e}")
        return {}


async def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description="Servidor MCP Python")
    parser.add_argument("--host", default="localhost", help="Host del servidor")
    parser.add_argument("--port", type=int, default=8000, help="Puerto del servidor")
    parser.add_argument("--config", help="Archivo de configuración personalizado")
    parser.add_argument("--debug", action="store_true", help="Modo debug")
    
    args = parser.parse_args()
    
    # Cargar configuración
    config = cargar_configuracion(args.config)
    server_config = config.get("server", {})
    
    # Usar argumentos de línea de comandos o configuración
    host = args.host or server_config.get("host", "localhost")
    port = args.port or server_config.get("port", 8000)
    debug = args.debug or server_config.get("debug", False)
    
    # Crear y configurar servidor
    server_name = server_config.get("name", "mcp-server")
    server_version = server_config.get("version", "0.1.0")
    
    server = MCPServer(name=server_name, version=server_version)
    
    print(f"🚀 Iniciando {server_name} v{server_version}")
    print(f"📍 Dirección: http://{host}:{port}")
    print(f"🔧 Modo debug: {'Activado' if debug else 'Desactivado'}")
    print(f"📊 Herramientas registradas: {len(server.tools)}")
    print(f"📄 Recursos registrados: {len(server.resources)}")
    print(f"💬 Prompts registrados: {len(server.prompts)}")
    print("\n" + "="*50)
    print("Presiona Ctrl+C para detener el servidor")
    print("="*50 + "\n")
    
    try:
        await server.start(host=host, port=port)
    except KeyboardInterrupt:
        print("\n👋 Deteniendo servidor...")
    except Exception as e:
        print(f"❌ Error al iniciar servidor: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
