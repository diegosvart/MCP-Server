"""
Tests para prompts MCP
"""

import pytest
from src.mcp_server.prompts import prompt_registry


def test_prompt_registry():
    """Test del registro de prompts"""
    # Verificar que los prompts por defecto están registrados
    prompts = prompt_registry.list_prompts()
    assert "greeting" in prompts
    assert "help_request" in prompts
    assert "error_response" in prompts


def test_render_greeting_prompt():
    """Test de renderizado del prompt greeting"""
    result = prompt_registry.render_prompt("greeting", {"name": "Usuario"})
    assert result == "Hola, soy Usuario. ¿En qué puedo ayudarte hoy?"


def test_render_error_response_prompt():
    """Test de renderizado del prompt error_response"""
    variables = {
        "error_message": "Error de conexión",
        "error_details": "No se pudo conectar al servidor"
    }
    result = prompt_registry.render_prompt("error_response", variables)
    assert "Error de conexión" in result
    assert "No se pudo conectar al servidor" in result


def test_render_prompt_missing_variable():
    """Test de renderizado con variable faltante"""
    result = prompt_registry.render_prompt("greeting", {})
    assert "Error: Variable faltante" in result


def test_get_nonexistent_prompt():
    """Test de obtener prompt inexistente"""
    result = prompt_registry.render_prompt("nonexistent_prompt")
    assert result is None
