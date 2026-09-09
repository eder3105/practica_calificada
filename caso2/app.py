import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def consultar_padron():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    try:
        # Ejemplo de prueba automatizada simulando consulta electoral ONPE
        driver.get("https://www.google.com")
        time.sleep(2)
        print("Automatización con Selenium ejecutada con éxito dentro del contenedor.")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Iniciando proceso de automatización...")
    consultar_padron()