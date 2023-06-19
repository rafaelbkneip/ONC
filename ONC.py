import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep

ouro = []
prata = []
bronze = []

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

                cont_ouro = 1
                cont_prata = 1
                cont_bronze = 1

                controle_ouro = True

                while(controle_ouro):
                    try: 
                        ouro.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[1]/div/table/tbody/tr/td[' + str(cont_ouro) +']').text)
                        ouro.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[1]/div/table/tbody/tr/td[' + str(cont_ouro+1) +']').text)
                        cont_ouro = cont_ouro + 1
                        
                    except:
                        print("Nenhuma medalha")
                        controle_ouro = False

                print(ouro)

                # try: 
                #     prata.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr/td[' + str(cont_prata) +']').text)
                #     prata.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr/td[' + str(cont_prata+1) +']').text)
                #     cont_prata = cont_prata + 1
                    
                # except:
                #     #pass
                #     print("Sem medalha :(")

                # try: 
                #     bronze.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[' + str(cont_bronze) +']').text)
                #     bronze.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[' + str(cont_bronze+1) +']').text)
                #     cont_bronze = cont_bronze + 1
                    
                # except:
                #     #pass
                #     print("Sem medalha :(")
                    
                navegador.back()

            except:
                controle = False


        cont_cidade = 1 + cont_cidade
    
        navegador.get("https://resultado.onciencias.org/estado/2022/" + brazilian_states.brazilian_states(12))


    except:
        controle_cidade = False

#Voltar a página anterior / Go back to the previous page
#navegador.back()