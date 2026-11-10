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

def renomear_colunas(dados, key_mapping):

    novos_dados = [{key_mapping.get(chaveAntiga): valor for chaveAntiga, valor in dictAntigo.items()} for dictAntigo in dados]
    return novos_dados

def get_columns(dados):
    return list(dados[-1].keys())

def size_dados(dados):
    return len(dados)

def join(dadosA, dadosB):
    lista_combinada = []

    lista_combinada.extend(dadosA)
    lista_combinada.extend(dadosB)
    return lista_combinada

def transformar_em_tabela(dados, colunas):
    dados_combinados_tabela = [colunas]

    for row in dados:
        linha = []
        for coluna in colunas:
            linha.append(row.get(coluna, 'Indisponível'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def salvar_dados(dados, path):

    with open(path, 'w') as file: 
        escritor = csv.writer(file)
        escritor.writerows(dados)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_injestao = 'data_processed/dados_combinados.csv'


# Leitura dos dados

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_json = leitura_dados(path_json, 'json')
dados_csv = leitura_dados(path_csv, 'csv')

colunas_json = get_columns(dados_json)
colunas_csv = get_columns(dados_csv)

dados_csv = renomear_colunas(dados_csv, key_mapping)

dados_unificados = join(dados_json, dados_csv)

colunas_referencia = colunas_csv


# Salvando Dados

dados_fusao_tabela = transformar_em_tabela(dados_unificados, colunas_referencia)
salvar_dados(dados_fusao_tabela, path_injestao)


### Validação

print(f"Colunas JSON: {colunas_json}")
print(f"Colunas CSV: {colunas_csv}")
print(f"Size CSV: {size_dados(dados_csv)}, Size JSON: {size_dados(dados_json)}, Size unificados: {size_dados(dados_unificados)}")
print(f"Dados Unificados: {dados_unificados[0], dados_unificados[-1]}")
print(dados_fusao_tabela[0], dados_fusao_tabela[-1])
