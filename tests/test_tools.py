"""
Tests para herramientas MCP
"""

import pytest
from src.mcp_server.tools import tool_registry, echo_tool, datetime_tool, json_formatter_tool, calculator_tool


def test_echo_tool():
    """Test de la herramienta echo"""
    result = echo_tool("Hello World")
    assert result == "Echo: Hello World"


def test_datetime_tool():
    """Test de la herramienta datetime"""
    result = datetime_tool()
    assert isinstance(result, str)
    # Verificar que es un formato ISO válido
    from datetime import datetime
    datetime.fromisoformat(result)  # Esto lanzará excepción si no es válido


def test_json_formatter_tool():
    """Test de la herramienta json formatter"""
    test_data = {"name": "test", "value": 123}
    result = json_formatter_tool(test_data)
    assert '"name": "test"' in result
    assert '"value": 123' in result


def test_calculator_tool():
    """Test de la herramienta calculadora"""
    assert calculator_tool("2 + 2") == "4"
    assert calculator_tool("10 * 5") == "50"
    assert calculator_tool("15 / 3") == "5.0"
    
    # Test de error con caracteres no permitidos
    result = calculator_tool("import os")
    assert "Error: Solo se permiten operaciones matemáticas básicas" in result


def test_tool_registry():
    """Test del registro de herramientas"""
    # Verificar que las herramientas por defecto están registradas
    tools = tool_registry.list_tools()
    assert "echo" in tools
    assert "datetime" in tools
    assert "json_formatter" in tools
    assert "calculator" in tools
    
    # Test de obtener herramienta
    echo_tool_info = tool_registry.get_tool("echo")
    assert echo_tool_info is not None
    assert echo_tool_info["function"] == echo_tool
