# Contribuir al Proyecto MCP Server

¡Gracias por tu interés en contribuir al proyecto MCP Server!

## Sobre el Autor

**Diego Morales** ([@diegosvart](https://github.com/diegosvart))  
- Ingeniero Informático AIEP  
- Diplomado en Machine Learning y Big Data PUC  
- AIEP (Título) | Pontificia Universidad Católica de Chile (Diplomado)  
- Email: moralesc.diego@gmail.com

## Cómo Contribuir

### 1. Fork del Repositorio
```bash
git clone https://github.com/diegosvart/MCP-Server.git
cd MCP-Server
```

### 2. Configurar Entorno de Desarrollo
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
pip install -e .
```

### 3. Ejecutar Pruebas
```bash
pytest tests/ -v
```

### 4. Crear una Rama
```bash
git checkout -b feature/nueva-caracteristica
```

### 5. Hacer Cambios y Commit
```bash
git add .
git commit -m "Descripción de los cambios"
```

### 6. Push y Pull Request
```bash
git push origin feature/nueva-caracteristica
```

Luego abre un Pull Request en GitHub.

## Estándares de Código

- **Idioma**: Código y comentarios en español
- **Estilo**: Seguir PEP 8
- **Pruebas**: Incluir pruebas unitarias para nuevas funcionalidades
- **Documentación**: Actualizar documentación cuando sea necesario

## Reportar Problemas

Si encuentras un bug o tienes una sugerencia:

1. Revisa si ya existe un issue similar
2. Crea un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Información del entorno (OS, Python version, etc.)

## Contacto

Para preguntas o colaboraciones directas:
- GitHub: [@diegosvart](https://github.com/diegosvart)
- Email: moralesc.diego@gmail.com

¡Esperamos tus contribuciones! 🚀
