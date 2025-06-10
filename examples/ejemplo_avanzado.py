"""
Ejemplo avanzado con herramientas personalizadas
"""

import asyncio
import json
import os
from datetime import datetime
from src.mcp_server.server import MCPServer


class CalculadoraAvanzada:
    """Herramientas de calculadora avanzada"""
    
    @staticmethod
    def operacion_compleja(expresion: str) -> str:
        """Evalúa expresiones matemáticas complejas de forma segura"""
        try:
            # Lista de funciones matemáticas permitidas
            import math
            funciones_permitidas = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'sqrt': math.sqrt,
                'log': math.log,
                'exp': math.exp,
                'pi': math.pi,
                'e': math.e
            }
            
            # Evaluar la expresión de forma segura
            resultado = eval(expresion, {"__builtins__": {}}, funciones_permitidas)
            return f"Resultado: {resultado}"
        except Exception as e:
            return f"Error en cálculo: {str(e)}"


class GestorArchivos:
    """Herramientas para gestión de archivos"""
    
    @staticmethod
    def listar_directorio(ruta: str = ".") -> str:
        """Lista el contenido de un directorio"""
        try:
            if not os.path.exists(ruta):
                return f"Error: La ruta {ruta} no existe"
            
            contenido = os.listdir(ruta)
            archivos = []
            directorios = []
            
            for item in contenido:
                ruta_completa = os.path.join(ruta, item)
                if os.path.isdir(ruta_completa):
                    directorios.append(f"📁 {item}/")
                else:
                    size = os.path.getsize(ruta_completa)
                    archivos.append(f"📄 {item} ({size} bytes)")
            
            resultado = f"Contenido de {ruta}:\n"
            resultado += "\n".join(directorios + archivos)
            return resultado
        except Exception as e:
            return f"Error al listar directorio: {str(e)}"
    
    @staticmethod
    def info_archivo(ruta: str) -> str:
        """Obtiene información detallada de un archivo"""
        try:
            if not os.path.exists(ruta):
                return f"Error: El archivo {ruta} no existe"
            
            stat = os.stat(ruta)
            info = {
                "nombre": os.path.basename(ruta),
                "ruta_completa": os.path.abspath(ruta),
                "tamaño": stat.st_size,
                "modificado": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "creado": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                "es_directorio": os.path.isdir(ruta)
            }
            
            return json.dumps(info, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Error al obtener información: {str(e)}"


async def ejemplo_avanzado():
    """Ejemplo avanzado con herramientas personalizadas"""
    server = MCPServer(name="servidor-avanzado", version="2.0.0")
    
    # Instanciar clases de herramientas
    calc = CalculadoraAvanzada()
    gestor = GestorArchivos()
    
    # Registrar herramientas de calculadora avanzada
    server.register_tool(
        "calc_avanzada",
        calc.operacion_compleja,
        "Calculadora que soporta funciones matemáticas como sin, cos, sqrt, etc."
    )
    
    # Registrar herramientas de gestión de archivos
    server.register_tool(
        "listar_dir",
        gestor.listar_directorio,
        "Lista el contenido de un directorio"
    )
    
    server.register_tool(
        "info_archivo",
        gestor.info_archivo,
        "Obtiene información detallada de un archivo"
    )
    
    # Registrar recursos dinámicos
    def obtener_estadisticas_sistema():
        """Obtiene estadísticas del sistema en tiempo real"""
        return {
            "timestamp": datetime.now().isoformat(),
            "directorio_actual": os.getcwd(),
            "variables_entorno": len(os.environ),
            "herramientas_registradas": len(server.tools),
            "recursos_registrados": len(server.resources)
        }
    
    server.register_resource(
        "stats_sistema",
        obtener_estadisticas_sistema(),
        "Estadísticas del sistema en tiempo real"
    )
    
    # Registrar prompts avanzados
    server.register_prompt(
        "reporte_calculo",
        """
        📊 REPORTE DE CÁLCULO
        ===================
        
        Expresión: {expresion}
        Resultado: {resultado}
        Timestamp: {timestamp}
        
        Detalles técnicos:
        - Tipo de operación: {tipo}
        - Tiempo de ejecución: {tiempo}ms
        """,
        "Prompt para reportes de cálculos matemáticos"
    )
    
    server.register_prompt(
        "reporte_archivo",
        """
        📁 INFORMACIÓN DE ARCHIVO
        ========================
        
        Archivo: {nombre}
        Ruta: {ruta}
        Tamaño: {tamaño} bytes
        Modificado: {modificado}
        
        Estado: {estado}
        """,
        "Prompt para reportes de información de archivos"
    )
    
    print("🚀 Servidor avanzado configurado!")
    print(f"📱 Herramientas disponibles: {len(server.tools)}")
    print(f"📄 Recursos disponibles: {len(server.resources)}")
    print(f"💬 Prompts disponibles: {len(server.prompts)}")
    print("\nEjemplos de uso:")
    print("- calc_avanzada('sqrt(16) + sin(pi/2)')")
    print("- listar_dir('.')")
    print("- info_archivo('README.md')")


if __name__ == "__main__":
    asyncio.run(ejemplo_avanzado())
