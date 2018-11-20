import httplib2 as http
import json
from collections import namedtuple

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}
uri = 'http://localhost:8080/rest/webresources'

def getMetodo(endereco):
    path = endereco
    target = urlparse(uri+path)
    method = 'GET'
    body = ''
    h = http.Http()
    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)
    return content

def putMetodo(endereco):
    path = endereco
    target = urlparse(uri+path)
    method = 'PUT'
    body = ''
    h = http.Http()
    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)
    return content
# assume that content is a json reply
# parse content with the json module
def ConsultarPassagem():
    print('Consultando Passagens...')
    data = json.loads(getMetodo('/Passagens/todas'))
    for x in data['passagens']:
        print('ID: ' + str(x['id']) + ' /De: ' + str(x['origem']) + ' /Para: ' + str(x['destino']) + ' /Data de Partida: ' + str(x['data']) + ' /Valor: ' + str(x['valor']) + ' /Acentos disponiveis: ' + str(x['poltronas']))

def ConsultarHospedagem():
    print('Consultando Hoteis...')
    data = json.loads(getMetodo('/Hospedagem/todas'))
    for x in data['hospedagens']:
        print('ID: ' + str(x['id']) + ' /Nome: ' + str(x['nomehotel']) + ' /Localizacao: ' + str(x['cidade']) + ' /Quartos Disponiveis: ' + str(x['quantidadequartos']) + ' /Pessoas por quarto: ' + str(x['numeromaxpessoas']) + ' /Valor: ' + str(x['valor']))
def ConsultarPacote():
    print('Consultando Pacotes...')
    data = json.loads(getMetodo('/Pacotes/todas'))
    for x in data['pacotes']:
        print('ID: ' + str(x['id']) + ' /Passagem ID: ' + str(x['passagemID']) + ' /Hotel ID: ' + str(x['hotelID']) + ' /Valor: ' + str(x['valor']) + ' /Quantidade de Pessoas: ' + str(x['qantidadePessoas']))
def ComprarPassagem():
    id = input('Digite o ID da passagem: ')
    quantidade = input('Digite a quantidade de poltronas')
    data = json.loads(putMetodo('/Passagens/{id}/{quantidade}'.format(id=id, quantidade=quantidade)))
    print(data)

def ReservarHotel():
    id = input('Digite o ID do hotel: ')
    quantidade = input('Digite a quantidade de pessoas')
    data = json.loads(putMetodo('/Hospedagem/{id}/{quantidade}'.format(id=id, quantidade=quantidade)))
    print(data)

def ComprarPacote():
    id = input('Digite o ID do pacote: ')
    data = json.loads(putMetodo('/Pacotes/{id}'.format(id=id)))
    print(data)

switcher = {
    1 : ConsultarPassagem,
    2 : ConsultarHospedagem,
    3 : ConsultarPacote,
    4 : ComprarPassagem,
    5 : ReservarHotel,
    6 : ComprarPacote,
}

while True:
    resposta = input('1 - ConsultarPassagem \n'
                     '2 - ConsultarHospedagem \n'
                     '3 - ConsultarPacotes \n'
                     '4 - ComprarPassagem\n'
                     '5 - ReservarHotel\n'
                     '6 - ComprarPacote\n')
    switcher[int(resposta)]()