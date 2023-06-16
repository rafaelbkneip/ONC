import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep

import brazilian_states

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
navegador.get("https://resultado.onciencias.org/estado/2022/" + brazilian_states.brazilian_states(12))


WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/a')))

cont_cidade = 1
controle_cidade = True

while(controle_cidade):

    try:
        link = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/table/tbody/tr['+str(cont_cidade)+']/td[1]/a').get_attribute('href')
        navegador.get(link)
        sleep(3)

        cont_escola = 1
        controle = True


        while(controle):

            try:
                sleep(1)
                navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/table/tbody/tr['+ str(cont_escola) +']/td[1]/a').click()
                cont_escola = cont_escola + 1

                try: 
                    resultado = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div/div/h3').text
                    print(resultado)

                except:
                    print("Error")

                navegador.back()

            except:
                controle = False


        cont_cidade = 1 + cont_cidade
    
        navegador.get("https://resultado.onciencias.org/estado/2022/" + brazilian_states.brazilian_states(12))


    except:
        controle_cidade = False

#Voltar a página anterior / Go back to the previous page
#navegador.back()

