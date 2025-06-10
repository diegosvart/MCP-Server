"""
MCP Server - Python Implementation

Este módulo implementa un servidor del Protocolo de Contexto de Modelo (MCP)
que permite la integración con clientes compatibles.

Autor: Diego Morales - Ingeniero Informático (PUC Chile)
Diplomado en Machine Learning y Big Data
Email: moralesc.diego@gmail.com
GitHub: @diegosvart
"""

__version__ = "0.1.0"
__author__ = "Diego Morales"
__email__ = "moralesc.diego@gmail.com"

from .server import MCPServer

__all__ = ["MCPServer"]
