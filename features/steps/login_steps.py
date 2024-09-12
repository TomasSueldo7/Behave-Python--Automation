from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

@given('the user is on the login page')
def open_login_page(context):
    # Inicialización de la página de login usando el driver del context
    context.login_page = LoginPage(context.driver)
    context.login_page.load()  # Navega a la página de login

@when('the user logs in with valid credentials')
def login(context):
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.submit()

@then('the system shows the home page')
def open_home_page(context):
    # Espera explícita para que la URL contenga la parte esperada
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("logged-in-successfully")
    )
    assert "https://practicetestautomation.com/logged-in-successfully/" in context.driver.current_url

@when('the user logs in with {user} and {password}')
def login_failed(context, user, password):
    context.login_page.enter_username(user)
    context.login_page.enter_password(password)
    context.login_page.submit()

@then('the system shows an error')
def login_error(context):
    error_element = context.driver.find_element(By.ID, "error")
    assert error_element.text in 'Your username is invalid!',  f"Texto encontrado: '{error_element.text}'"

