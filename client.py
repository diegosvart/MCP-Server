#!/usr/bin/env python3
"""
Cliente interactivo para el servidor MCP
Permite ejecutar herramientas del servidor desde línea de comandos
"""

import requests
import json
import sys
import argparse
from typing import Dict, Any
import time


class MCPClient:
    """Cliente para interactuar con el servidor MCP"""
    
    def __init__(self, base_url: str = "http://localhost:8001"):
        self.base_url = base_url.rstrip('/')
        
    def check_server(self) -> bool:
        """Verificar si el servidor está funcionando"""
        try:
            response = requests.get(f"{self.base_url}/", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_server_info(self) -> Dict[str, Any]:
        """Obtener información del servidor"""
        try:
            response = requests.get(f"{self.base_url}/")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def list_tools(self) -> Dict[str, Any]:
        """Listar herramientas disponibles"""
        try:
            response = requests.get(f"{self.base_url}/tools")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def list_resources(self) -> Dict[str, Any]:
        """Listar recursos disponibles"""
        try:
            response = requests.get(f"{self.base_url}/resources")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def list_prompts(self) -> Dict[str, Any]:
        """Listar prompts disponibles"""
        try:
            response = requests.get(f"{self.base_url}/prompts")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}


def print_json(data: Any, title: str = ""):
    """Imprimir datos JSON de forma legible"""
    if title:
        print(f"\n🔹 {title}")
        print("=" * (len(title) + 4))
    
    if isinstance(data, dict) and "error" in data:
        print(f"❌ Error: {data['error']}")
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(
        description="Cliente para interactuar con el servidor MCP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python client.py info                     # Información del servidor
  python client.py tools                    # Listar herramientas
  python client.py resources                # Listar recursos
  python client.py prompts                  # Listar prompts
  python client.py --url http://localhost:8001 info  # Servidor en puerto específico
        """
    )
    
    parser.add_argument(
        "command",
        choices=["info", "tools", "resources", "prompts", "check"],
        help="Comando a ejecutar"
    )
    
    parser.add_argument(
        "--url",
        default="http://localhost:8001",
        help="URL del servidor MCP (default: http://localhost:8001)"
    )
    
    args = parser.parse_args()
    
    client = MCPClient(args.url)
    
    # Verificar conexión
    print(f"🔍 Conectando a {args.url}...")
    
    if not client.check_server():
        print(f"❌ No se pudo conectar al servidor en {args.url}")
        print("💡 Asegúrate de que el servidor esté ejecutándose:")
        print("   python -m mcp_server.server")
        sys.exit(1)
    
    print("✅ Conexión exitosa")
    
    # Ejecutar comando
    if args.command == "check":
        print("✅ El servidor está funcionando correctamente")
        
    elif args.command == "info":
        info = client.get_server_info()
        print_json(info, "Información del Servidor")
        
    elif args.command == "tools":
        tools = client.list_tools()
        print_json(tools, "Herramientas Disponibles")
        
    elif args.command == "resources":
        resources = client.list_resources()
        print_json(resources, "Recursos Disponibles")
        
    elif args.command == "prompts":
        prompts = client.list_prompts()
        print_json(prompts, "Prompts Disponibles")


if __name__ == "__main__":
    main()
