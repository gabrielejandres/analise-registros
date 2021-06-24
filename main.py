import requests

def getCountryByCode(code):
    response = requests.get(f'https://restcountries.eu/rest/v2/callingcode/{code}')
    if response.status_code != 200:
        raise Exception('Erro ao consultar API de códigos DDI')
    else:
        response = response.json()
        return response[0]['translations']['br']

def updateDataOfCountry(country, status):
    if usersByCountry.get(country) is None:
        usersByCountry[country] = activesByCountry[country] = 0

    usersByCountry[country] += 1
    if status == "assinado":
        activesByCountry[country] += 1

def handleFileReading(nameOfFile):
    file = open(nameOfFile, 'r')

    for line in file:
        ddi = line[0] + line[1]
        status = line.split()[1]
        country = getCountryByCode(ddi)

        updateDataOfCountry(country, status)

    file.close()

def createReportFile():
    newFile = open("out.txt", "w")

    for key in usersByCountry:
        line = key + ", " + str(usersByCountry[key]) + ", " + str(activesByCountry[key]) + "\n"
        newFile.write(line)

    print("Análise dos dados enviada para o arquivo out.txt")
    newFile.close()

usersByCountry = {}
activesByCountry = {}

name = input("Digite o nome do arquivo de registros de entrada: ")
handleFileReading(name)
createReportFile()
