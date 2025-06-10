# MCP Server - Python Implementation

Un servidor del Protocolo de Contexto de Modelo (MCP) implementado en Python.

**Autor**: Diego Morales ([@diegosvart](https://github.com/diegosvart))  
**Título**: Ingeniero Informático, Diplomado en Machine Learning y Big Data  
**Institución**: Pontificia Universidad Católica de Chile  
**Email**: moralesc.diego@gmail.com  

## Descripción

Este proyecto implementa un servidor MCP que permite la integración con clientes compatibles como Claude Desktop, VS Code Extensions, y otras aplicaciones que soportan el protocolo MCP.

## Características

- ✅ Soporte para Herramientas (Tools)
- ✅ Soporte para Recursos (Resources) 
- ✅ Soporte para Prompts
- ⚠️ Descubrimiento (Discovery) - En desarrollo
- ❌ Sampling - Planeado
- ❌ Roots - Planeado

## Estructura del Proyecto

```
MCP-Server/
├── src/
│   └── mcp_server/
│       ├── __init__.py
│       ├── server.py
│       ├── tools/
│       ├── resources/
│       └── prompts/
├── tests/
├── docs/
├── examples/
├── config/
├── requirements.txt
├── setup.py
└── README.md
```

## Instalación

```bash
pip install -r requirements.txt
pip install -e .
```

## Uso

```bash
python -m mcp_server
```

## Configuración

La configuración del servidor se encuentra en el directorio `config/`.

## Desarrollo

### Ejecutar tests
```bash
pytest tests/
```

### Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

MIT License
