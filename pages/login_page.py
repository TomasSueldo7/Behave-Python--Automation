from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

class LoginPage:
    URL = os.getenv("URL")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL) #Navegación a la URL

    def enter_username(self, username):
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

    def submit(self):
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()