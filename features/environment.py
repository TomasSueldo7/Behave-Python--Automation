from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Cargar las variables de entorno
load_dotenv()

def iniciar_navegador():
    # Configuración de opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # Para abrir el navegador maximizado

    # Configuración del servicio de ChromeDriver usando webdriver-manager
    service = Service(ChromeDriverManager().install())

    # Inicialización del navegador con el servicio y las opciones
    return webdriver.Chrome(service=service, options=chrome_options)

def before_scenario(context, scenario):
    # Iniciar el navegador antes de cada escenario
    context.driver = iniciar_navegador()

def after_step(context, step):
    if step.status == "failed":
        screenshot_dir = 'reports/screenshots'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f'failure_{step.name}.png')
        print(f"Capturando screenshot: {screenshot_path}")  # Mensaje de depuración
        context.driver.save_screenshot(screenshot_path)

def after_scenario(context, scenario):
    # Cerrar el navegador después de cada escenario
    if hasattr(context, 'driver'):
        context.driver.quit()