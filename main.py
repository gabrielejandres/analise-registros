import requests

def getCountryByCode(code):
    '''
        Returns the country corresponding to the IDD code entered

        :param code: String with IDD code
        :return: The country
    '''

    response = requests.get(f'https://restcountries.eu/rest/v2/callingcode/{code}')

    if response.status_code == 200:
        response = response.json()
        return response[0]['translations']['br']
    else:
        raise Exception('Erro ao consultar API de códigos DDI')


def updateDataOfCountry(country, status):
    '''
        Updates the total number of users and number of active users by country

        :param country: The country with data to be updated
        :param status: User status indicating if it is active or not
    '''

    if usersByCountry.get(country) is None:
        usersByCountry[country] = activesByCountry[country] = 0

    usersByCountry[country] += 1
    if status == "assinado":
        activesByCountry[country] += 1


def handleFileReading(nameOfFile):
    '''
        Reads the input file and identifies information needed to update each country's data

        :param nameOfFile: Input file name
    '''

    file = open(nameOfFile, 'r')

    for line in file:
        idd = line[0] + line[1]
        status = line.split()[1]
        country = getCountryByCode(idd)

        updateDataOfCountry(country, status)

    file.close()


def createReportFile():
    '''
        Creates a report file with the total number of users and the number of active users in each country
    '''

    newFile = open("out.txt", "w")

    for key in usersByCountry:
        line = key + ", " + str(usersByCountry[key]) + ", " + str(activesByCountry[key]) + "\n"
        newFile.write(line)

    print("Análise dos dados enviada para o arquivo out.txt")
    newFile.close()


# Dictionaries to associate the total number of users and the number of active users per country
usersByCountry = {}
activesByCountry = {}

# Main flow
name = input("Digite o nome do arquivo de registros de entrada: ")
handleFileReading(name)
createReportFile()
