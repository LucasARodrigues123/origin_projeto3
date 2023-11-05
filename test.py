import json
from cadastro_funsão import minha_funcao
dados_carregados = minha_funcao()
# Abra o arquivo JSON
with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
# Verifique se os dados são uma lista de dicionários
if isinstance(dados, list):
    numero_de_pessoas = len(dados)
    print(f"O arquivo JSON contém {numero_de_pessoas} pessoas.")
else:
    print("O arquivo JSON não contém uma lista de pessoas ou um dicionário de pessoas.") 


def buscar(dados_carregados, entrada):
    lista_client = []
    for Client in dados_carregados:
        if Client.get('Client','').lower() == entrada.lower():
            lista_client.append(Client)
    return lista_client

entrada = input('Digite o nome do Cliente que procura?:')

lista_client = buscar(dados_carregados, entrada)

if lista_client:
    print(lista_client)
    for client in lista_client:
        print("Nome:",client.get("Client"))
        print("Idade:",client.get("Idade"))
        print("Peso:",client.get("Peso"))
        print("Altura:",client.get("Altura"))
        print("Nacimento:",client.get("Nacimento"))
        print("Cpf:",client.get("Cpf"))
        print("Cidade:",client.get("Cidade"))
        print("Email:",client.get("Email"))
            
else:
    print("Nenhum cliente encontrado com o nome especificado.")
    




    
    

    







