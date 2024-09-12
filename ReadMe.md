# Behave-Python Automation Scaffolding

Este proyecto es un scaffolding para pruebas automatizadas utilizando `Behave` para facilitar la creación de proyectos de automatización de pruebas con Python. Está diseñado para manejar proyectos de pruebas E2E y generar reportes con Allure.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **Behave**: Framework de pruebas BDD (Behavior-Driven Development).
- **Selenium**: Para la automatización del navegador.
- **Allure**: Para la generación de reportes de pruebas.
- **dotenv**: Para manejar variables de entorno.

## Objetivo

El objetivo de este proyecto es proveer un scaffolding sencillo y funcional que permita implementar pruebas automatizadas de forma eficiente, integrando Selenium para la ejecución de acciones en navegadores y Behave para la escritura de pruebas en un estilo BDD. Además, se generan reportes detallados con Allure.

## Requisitos Previos

Asegúrate de tener las siguientes herramientas instaladas en tu máquina:

- Python (>=3.6)
- pip (Gestor de paquetes de Python)
- Google Chrome (última versión)
- WebDriver Manager (manejado automáticamente por el proyecto)

## Instalación

1. **Clonar el repositorio**
2. **Navegar a la carpeta del proyecto**
3. **Instalar dependencias:** pip install -r requirements.txt

## Variables de entorno
Este proyecto utiliza dotenv para cargar variables de entorno desde un archivo .env. Asegúrate de crear un archivo .env en la raíz del proyecto con las siguientes variables:

- USERNAME=student
- PASSWORD=Password123
- URL=https://practicetestautomation.com/practice-test-login/

**IMPORTANTE: El archivo .ENV debe agregarse en el .gitignore.**

## Ejecución de proyectos

Para ejecutar las pruebas BDD definidas con Behave, usa el siguiente comando: behave

## Reportes con allure

1. **Ejecutar las pruebas**
2. **Generar el reporte en HTML:** allure generate 
3. **Abrir el reporte:** allure open reports/allure-html

