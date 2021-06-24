# An�lise de registros
*Dado um arquivo de entrada qualquer, contendo n�meros de telefone e um status do usu�rio, 
o projeto utiliza a API externa https://restcountries.eu/ para fornecer um arquivo 
de sa�da com a an�lise dos dados presentes na entrada, informando:*
* *Quantos usu�rios usaram o servi�o em cada pa�s?*
* *Quantos usu�rios ativos (cujo �ltimo status foi �assinado�) existem em cada pa�s?*
 
## Tabela de Conte�do

 1. [Tecnologias utilizadas](#tecnologias-utilizadas)
 2. [Instala��o](#instala��o)
 3. [Uso](#uso)
 
## Tecnologias utilizadas

Essas s�o as ferramentas utilizadas e que s�o necess�rias para instalar e 
rodar o projeto:

 - Python, vers�o 3.7
 - pip, vers�o 21.2.2
 - PyCharm, 2021 (recomendado, mas n�o necess�rio)

![Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Badge](https://img.shields.io/badge/pip-544327?style=for-the-badge)
![Badge](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

## Instala��o 

*1. Clone esse reposit�rio*
``` bash
git clone https://github.com/gabrielejandres/analise-registros.git
```

*2. No seu terminal, navegue at� esse reposit�rio*

*3. Para conseguirmos nos comunicar com a API externa iremos precisar da biblioteca 
requests, como essa biblioteca n�o � built in do Python, vamos instal�-la atrav�s 
do comando*

``` bash
$ pip install requests 
```

*4. Finalmente, para executar o programa, digite no terminal*

``` bash
$ python main.py
```

*5. Ou, se preferir, utilize o PyCharm para rodar o projeto*

*Voc� pode utilizar o arquivo in.txt padr�o fornecido com entrada, ou adicionar outros
arquivos de entrada de sua prefer�ncia*
 
## Uso

*Os arquivos de entrada devem seguir a seguinte formata��o:*

```
<telefone com ddi e ddd> <status>
```
* *Exemplo:*
```
55211298371229 cancelado
56389428347834 assinado
52211298371229 assinado
55757575756432 cancelado
56121298371289 cancelado
```

*O arquivo de sa�da com a an�lise dos registros ter� a seguinte formata��o:*

```
<nome do pa�s>, <n�mero de usu�rios>, <n�mero de usu�rios ativos>
```
* *Exemplo:*
```
Brasil, 2, 0
Chile, 2, 1
M�xico, 1, 1
```

### �ltima atualiza��o: 24/06/2021
