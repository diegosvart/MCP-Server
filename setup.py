from setuptools import setup, find_packages

setup(
    name="mcp-server",
    version="0.1.0",
    description="Servidor del Protocolo de Contexto de Modelo implementado en Python",
    author="Diego Morales - Ingeniero Informático (PUC Chile)",
    author_email="moralesc.diego@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",    install_requires=[
        "pydantic>=2.0.0",
        "uvicorn>=0.24.0",
        "fastapi>=0.104.0",
        "typing-extensions>=4.0.0",
        "aiohttp>=3.8.0",
        "websockets>=11.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "mcp-server=mcp_server.server:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
