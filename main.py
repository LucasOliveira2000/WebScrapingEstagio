from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("http://200.198.139.228/leiloeiros/busca")

try:
    time.sleep(2)
    pesquisar = navegador.find_element(By.XPATH, ".//button[@class='btn btn-primary']").click()

    time.sleep(2)
    conteudos = navegador.find_elements(By.XPATH, '//b')


    for conteudo in conteudos:

        time.sleep(5)
        nome = conteudo.find_element(By.XPATH, '/html/body/div[2]/b').text
        time.sleep(5)
        print(nome)

        navegador.quit()

except NoSuchElementException:
    print("Valor não encontrado")
    navegador.quit()