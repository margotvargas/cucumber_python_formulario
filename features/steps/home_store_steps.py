import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('usuario está en página formulario contacto')
def iniciar_navegador(context): #Iniciar el navegador
    context.driver = webdriver.Chrome()
    context.driver.get("http://www.automationpractice.pl/index.php?controller=contact")

@when('ingresa campos "{email}" "{orden}" "{msj}"')
def ingresar_campos(context, email, orden, msj):
    # Espera hasta que el elemento sea visible antes de verificar su presencia
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
    context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email) #Ingresa el email
    context.driver.find_element(By.XPATH, "//input[@id='id_order']").send_keys(orden) #Ingresa la Orden de referencia
    context.driver.find_element(By.XPATH, "//textarea[@id='message']").send_keys(msj) #Ingresa el mensaje
    context.driver.find_element(By.XPATH, "//select[@id='id_contact']/option[@value='2']").click() #Selecciona la opcion Customer Services

@when('click en boton enviar')
def click_enviar(context):
    context.driver.find_element(By.XPATH, "//button[@id='submitMessage']").click()

@then('obtiene mensaje confirmacion exitosa')
def obtener_mensaje_confirmacion(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='alert alert-success']"))
    )
    mensaje_confirmacion = context.driver.find_element(By.XPATH, "//p[@class='alert alert-success']").text
    assert "Your message has been successfully sent" in mensaje_confirmacion
    time.sleep(2)

def cerrar_navegador(context):
    context.driver.close()


