#Módulo para salvar lista em um arquivo xlsx / Module to save the list to an xlsx file

#Importações / Imports
import xlsxwriter

#Função para salvar o arquivo / Function to save thee file
def salvar(unica, estado):

    #Escrever o arquivo / Write the file
    workbook = xlsxwriter.Workbook('ONC-'+ estado + '.xlsx')
    #Adicionar uma aba / Add a sheet
    sheet = workbook.add_worksheet()   

    cont_linha = 0
    cont = -1

    try:
        #Cada elemento da lista tornará-se uma linha do documento / Each list element will be a row in the file
        while (cont < len(unica)-6):
           
                sheet.write(cont_linha + 1, 0, unica[cont+1])
                sheet.write(cont_linha + 1, 1, unica[cont+2])
                sheet.write(cont_linha + 1, 2, unica[cont+3])
                sheet.write(cont_linha + 1, 3, unica[cont+4])
                sheet.write(cont_linha + 1, 4, unica[cont+5])
                sheet.write(cont_linha + 1, 5, unica[cont+6])

                cont = cont + 6
                cont_linha = cont_linha + 1

    except Exception as e:
        print(e)

    #Fechar o arquivo / Close the file
    workbook.close()

    return print("Finalizado!")