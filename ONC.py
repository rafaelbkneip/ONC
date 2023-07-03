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
import save

#Brazilians states / Estados brasileiros
for i in range (27):
    print(brazilian_states.brazilian_states(i))

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)

for i in range (27):

    unica = []
    ouro = []
    prata = []
    bronze = []

    #Acess the page for each brazilian state with its abbreviation / Acessar a página de cada estado brasileiro por meio de sua sigla
    navegador.get("https://resultado.onciencias.org/estado/2022/" + brazilian_states.brazilian_states(i))

    estado = brazilian_states.brazilian_states(i)

    #Make sure the page is fully loaded / Garantir que a página está totalmente carregada
    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/a')))

    #Counter for the cities in the state / Contador para as cidades desse estado
    cont_cidade = 1
    controle_cidade = True

    #For each city, access the page with each school / Para cada cidade, acessar a página com cada escola
    while(controle_cidade):

        try:
            #Access the page with all of the cities / Acessar a página de todas as cidades
            link = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/table/tbody/tr['+str(cont_cidade)+']/td[1]/a').get_attribute('href')
            navegador.get(link)
            sleep(3)
            cidade = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/h3').text

            cont_escola = 1
            controle = True

            #Access the page with all of the schools / Acessar a página de todas as cidades
            while(controle):

                try:
                    #For each school, check if there are medalists / Para cada escola, verificar se existem medalhistas
                    sleep(1)
                    navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/table/tbody/tr['+ str(cont_escola) +']/td[1]/a').click()
                    cont_escola = cont_escola + 1
                    
                    #Get the name of the school / Obter o nome da escola
                    escola = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/span').text

                    #Auxiliary counters / Contadores auxiliares
                    cont_ouro = 1
                    cont_prata = 1
                    cont_bronze = 1
                    
                    #Gold medal / Medalha de ouro
                    controle_ouro = True
                    #The medals are shown in tables - if the are tables, there are medalists / As medahas são mostradas em tabelas - se existem tabelas, exsitem medalihistas
                    while(controle_ouro):

                        try:
                            #Add the information to a list / Adicionar as infomrações à uma lista
                            ouro.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[1]/div/table/tbody/tr/td[' + str(cont_ouro) +']').text)
                            ouro.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[1]/div/table/tbody/tr/td[' + str(cont_ouro + 1) +']').text)
                            ouro.append(estado)
                            ouro.append(cidade)
                            ouro.append(escola)
                            ouro.append("Medalha de ouro")

                            cont_ouro = cont_ouro + 2

                        #No medalist student or end of the table / Nenhum aluno medalhista ou fim da tabela    
                        except:
                            print("Nenhuma medalha de ouro")
                            controle_ouro = False

                    # print(ouro)
                    # print(len(ouro))

                    #Silver medal / Medalha de prata 
                    controle_prata = True
                    while(controle_prata):

                        try:
                            prata.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr/td[' + str(cont_prata) +']').text)
                            prata.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr/td[' + str(cont_prata + 1) +']').text)
                            prata.append(estado)
                            prata.append(cidade)
                            prata.append(escola)
                            prata.append("Medalha de prata")
                        
                            cont_prata = cont_prata + 2
                            
                        except:
                            print("Nenhuma medalha de prata")
                            controle_prata = False

                    # print(prata)
                    # print(len(prata))

                    #Bronze medal / Medalha de bronze
                    controle_bronze = True
                    while(controle_bronze):

                        try:
                            bronze.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[' + str(cont_bronze) +']').text)
                            bronze.append(navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[' + str(cont_bronze + 1) +']').text)
                            bronze.append(estado)
                            bronze.append(cidade)
                            bronze.append(escola)
                            bronze.append("Medalha de bronze")
                        
                            cont_bronze = cont_bronze + 2
                            
                        except:
                            print("Nenhuma medalha de bronze")
                            controle_bronze = False

                    # print(bronze)
                    # print(len(bronze))
                    
                    #Get back to the page with all cities for this state / Voltar para página com todas as cidades desse estado
                    navegador.back()

                #End of the cities for this state / Fim da lista das cidades
                except:
                    controle = False

            cont_cidade = 1 + cont_cidade
        
            
            navegador.get("https://resultado.onciencias.org/estado/2022/" + brazilian_states.brazilian_states(i))


        #End of the cities fot this state
        except:
            controle_cidade = False

    #Create one single list with all of the medalists
    unica = ouro + prata + bronze

    #Save a .csv file for each state
    save.salvar(unica,  brazilian_states.brazilian_states(i))
