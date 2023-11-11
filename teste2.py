import json

try:
    with open("dados.json","r",encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    nome = "lucas"
    idade = 24
    altura = 1.70
    peso = 58
    nascimento = "30/05/1999"
    cpf = "13510225721"
    cidade = "curitiba"
    email = "lucas@gmail.com"

    # Criando um dicionário
    dados = [{
        "Nome":nome,
        "Idade": idade,
        "Altura": altura,
        "Peso": peso,
        "Nascimento": nascimento,
        "Cpf": cpf,
        "Cidade": cidade,
        "Email": email
    }]

    # Salvando o dicionário em um arquivo JSON
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo ,indent=4)

