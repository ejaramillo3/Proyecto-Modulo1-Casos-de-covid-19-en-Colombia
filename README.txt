# Proyecto: Consulta de Casos de COVID-19 en Colombia

Programa en Python que consulta los casos de COVID-19 en distintos departamentos de Colombia, usando la API pública de Datos Abiertos del Gobierno Colombiano.

## Autor
Clareth Jaramillo - Programación III

## Tecnologías
- Python 3.12
- pandas
- sodapy

## Estructura
- `api/consultas.py`: lógica de consulta a la API.
- `ui/__init__.py`: reservado para interfaz de usuario.
- `main.py`: punto de entrada.

## Cómo ejecutar
1. Crear un entorno virtual: `python -m venv venv`
2. Activar el entorno virtual: `.\venv\Scripts\Activate.ps1`
3. Instalar dependencias: `pip install pandas sodapy`
4. Ejecutar: `python main.py`
5. Ingresar el departamento y el número de registros.

## Ejemplo
Departamento: ANTIOQUIA
Registros: 10

## Fuente de datos
API de Datos Abiertos de Colombia: https://www.datos.gov.co
Dataset: gt2j-8ykr