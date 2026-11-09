import json
import csv


def leitura_json(path_json):
    dados_json= []

    with open(path_json, 'r') as file:
        dados_json = json.load(file) #lista de dict
    return dados_json

def leitura_csv(path_csv, delimitador):
    dados_csv = []

    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=delimitador)

        for linha in spamreader: 
            dados_csv.append(linha)

        return dados_csv

def leitura_dados(path_arquivo: str, tipo_arquivo: str):
    dados = []

    if tipo_arquivo == 'json':
        dados = leitura_json(path_json=path_arquivo)
        return dados

    elif tipo_arquivo == 'csv':
        dados = leitura_csv(path_csv=path_arquivo, delimitador=',')
        return dados


leitura_dados('data_raw/dados_empresaA.json', 'json')
leitura_dados('data_raw/dados_empresaB.csv', 'csv')

