# Análise de registros
*Dado um arquivo de entrada qualquer, contendo números de telefone e um status do usuário, 
o projeto utiliza a API externa https://restcountries.eu/ para fornecer um arquivo 
de saída com a análise dos dados presentes na entrada, informando:*
* *Quantos usuários usaram o serviço em cada país?*
* *Quantos usuários ativos (cujo último status foi “assinado”) existem em cada país?*
 
## Tabela de Conteúdo

 1. [Tecnologias utilizadas](#tecnologias-utilizadas)
 2. [Instalação](#instalação)
 3. [Uso](#uso)
 
## Tecnologias utilizadas

Essas são as ferramentas utilizadas e que são necessárias para instalar e 
rodar o projeto:

 - Python, versão 3.7
 - pip, versão 21.2.2
 - PyCharm, 2021 (recomendado, mas não necessário)

![Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Badge](https://img.shields.io/badge/pip-544327?style=for-the-badge)
![Badge](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

## Instalação 

*1. Clone esse repositório*
``` bash
git clone https://github.com/gabrielejandres/analise-registros.git
```

*2. No seu terminal, navegue até esse repositório*

*3. Para conseguirmos nos comunicar com a API externa iremos precisar da biblioteca 
requests, como essa biblioteca não é built in do Python, vamos instalá-la através 
do comando*

``` bash
$ pip install requests 
```

*4. Finalmente, para executar o programa, digite no terminal*

``` bash
$ python main.py
```

*5. Ou, se preferir, utilize o PyCharm para rodar o projeto*

*Você pode utilizar o arquivo in.txt padrão fornecido com entrada, ou adicionar outros
arquivos de entrada de sua preferência*
 
## Uso

*Os arquivos de entrada devem seguir a seguinte formatação:*

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

*O arquivo de saída com a análise dos registros terá a seguinte formatação:*

```
<nome do país>, <número de usuários>, <número de usuários ativos>
```
* *Exemplo:*
```
Brasil, 2, 0
Chile, 2, 1
México, 1, 1
```

### Última atualização: 24/06/2021
