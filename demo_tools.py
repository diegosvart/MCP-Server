#!/usr/bin/env python3
"""
Script de demostración para probar las herramientas de archivos del servidor MCP
"""

import requests
import json
import os


def test_mcp_tools():
    """Prueba las herramientas del servidor MCP"""
    base_url = "http://localhost:8001"
    
    print("🚀 Probando Herramientas del Servidor MCP")
    print("=" * 50)
    print()
      # Verificar conexión
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code != 200:
            print("❌ Error: Servidor no responde")
            return
        print("✅ Conectado al servidor MCP")
        
    except:
        print("❌ Error: No se puede conectar al servidor")
        print("💡 Asegúrate de que el servidor esté ejecutándose con: python server_enhanced.py")
        return
    
    def call_tool(tool_name, *args):
        """Llama a una herramienta del servidor MCP vía API"""
        try:
            payload = {
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": list(args) if len(args) > 1 else args[0] if args else {}
                }
            }
            response = requests.post(f"{base_url}/tools/call", json=payload)
            if response.status_code == 200:
                return response.json().get("content", [{}])[0].get("text", "Sin resultado")
            else:
                return f"Error HTTP {response.status_code}: {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

    # 1. Listar directorio actual
    print("📁 1. Listando directorio actual:")
    result = call_tool("list_directory", ".")
    print(result)
    print()
    
    # 2. Crear directorio de prueba
    print("📂 2. Creando directorio de prueba:")
    result = call_tool("create_directory", "test_mcp")
    print(result)
    print()
    
    # 3. Escribir archivo de prueba
    print("📝 3. Escribiendo archivo de prueba:")
    content = """# Archivo de prueba MCP
            Este es un archivo creado usando las herramientas del servidor MCP.

            Funcionalidades probadas:
            - ✅ Crear directorios
            - ✅ Escribir archivos
            - ✅ Leer archivos
            - ✅ Listar directorios

            Fecha: 2025-06-10
            """
    result = call_tool("write_file", "test_mcp/prueba.md", content)
    print(result)
    print()
    
    # 4. Leer el archivo creado
    print("📖 4. Leyendo archivo creado:")
    result = call_tool("read_file", "test_mcp/prueba.md")
    print(result)
    print()
    
    # 5. Obtener información del archivo
    print("ℹ️ 5. Información del archivo:")
    result = call_tool("get_file_info", "test_mcp/prueba.md")
    print(result)
    print()
    
    # 6. Buscar archivos
    print("🔍 6. Buscando archivos *.md:")
    result = call_tool("find_files", "*.md", ".")
    print(result)
    print()
    
    # 7. Copiar archivo
    print("📋 7. Copiando archivo:")
    result = call_tool("copy_file", "test_mcp/prueba.md", "test_mcp/copia_prueba.md")
    print(result)
    print()
    
    # 8. Listar contenido del directorio de prueba
    print("📁 8. Contenido del directorio de prueba:")
    result = call_tool("list_directory", "test_mcp")
    print(result)
    print()
    
    print("🎉 ¡Pruebas completadas!")
    print()
    print("💡 Comandos útiles:")
    print("   python demo_tools.py          # Ejecutar esta demostración")
    print("   python client.py info         # Información del servidor")
    print("   python client.py tools        # Lista de herramientas")
    print("   python server_enhanced.py     # Iniciar servidor")


if __name__ == "__main__":
    test_mcp_tools()
