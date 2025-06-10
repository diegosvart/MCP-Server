"""
Tests para el servidor MCP
"""

import pytest
import asyncio
from fastapi.testclient import TestClient
from src.mcp_server.server import MCPServer


@pytest.fixture
def server():
    """Crear instancia del servidor para tests"""
    return MCPServer(name="test-server", version="0.1.0")


@pytest.fixture
def client(server):
    """Crear cliente de test"""
    return TestClient(server.app)


def test_server_root(client):
    """Test del endpoint raíz"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test-server"
    assert data["version"] == "0.1.0"
    assert data["protocol"] == "model-context-protocol"


def test_list_tools(client):
    """Test del listado de herramientas"""
    response = client.get("/tools")
    assert response.status_code == 200
    data = response.json()
    assert "tools" in data


def test_list_resources(client):
    """Test del listado de recursos"""
    response = client.get("/resources")
    assert response.status_code == 200
    data = response.json()
    assert "resources" in data


def test_list_prompts(client):
    """Test del listado de prompts"""
    response = client.get("/prompts")
    assert response.status_code == 200
    data = response.json()
    assert "prompts" in data


def test_register_tool(server):
    """Test de registro de herramientas"""
    def test_func():
        return "test"
    
    server.register_tool("test_tool", test_func, "Test tool")
    assert "test_tool" in server.tools
    assert server.tools["test_tool"]["function"] == test_func
    assert server.tools["test_tool"]["description"] == "Test tool"


def test_register_resource(server):
    """Test de registro de recursos"""
    test_data = {"key": "value"}
    server.register_resource("test_resource", test_data, "Test resource")
    assert "test_resource" in server.resources
    assert server.resources["test_resource"]["data"] == test_data


def test_register_prompt(server):
    """Test de registro de prompts"""
    template = "Hello {name}"
    server.register_prompt("test_prompt", template, "Test prompt")
    assert "test_prompt" in server.prompts
    assert server.prompts["test_prompt"]["template"] == template
