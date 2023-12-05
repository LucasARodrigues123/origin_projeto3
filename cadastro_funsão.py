import json

def carregar_dados_json():
    try:
        with open("dados.json", 'r') as dados:
            dados_carregados = json.load(dados)
            numero_de_pessoas = len(dados_carregados)
            print(f"Número de objetos no banco de dados: {numero_de_pessoas}")
        return dados_carregados
    except FileNotFoundError:
        print("O arquivo 'dados.json' não foi encontrado.")
        

def minha_funcao():
    with open('dados.json','r') as arquivo:
        dados = json.load(arquivo)
    return dados
dados_carregados = minha_funcao()

def cadastro(lista, nome, idade, altura, peso, nascimento, cpf, cidade, email):
    nova_pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Altura": altura,
        "Peso": peso,
        "Cidade": cidade,
        "Nascimento": nascimento,
        "CPF": cpf,
        "Email": email,
    }
    nova_lista = []
    nova_lista.append(nova_pessoa)
    lista.append(nova_lista)

    with open('dados.json', 'w') as arquivo:
        json.dump(lista, arquivo, indent=4)


def buscar(dados_carregados, entrada):
    lista_client = []
    for nome in dados_carregados:
        if nome.get('Client','').lower() == entrada.lower():
            lista_client.update(nome)
    return lista_client

