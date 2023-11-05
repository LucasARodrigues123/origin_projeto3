import json
import cadastro_funsão
from cadastro_funsão import buscar
from cadastro_funsão import minha_funcao

client = "lucas"
idade = 24
altura = 1.70
peso = 58
nascimento = "30/05/1999"
cpf = "13510225721"
cidade = "curitiba"
email = "lucas@gmail.com"

# Criando um dicionário
dados = [{
    "Client": client,
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

# Abra o arquivo JSON
with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

# Verifique se os dados são uma lista de dicionários
if isinstance(dados, list):
    numero_de_pessoas = len(dados)
    print(f"O arquivo de Cadastro contém {numero_de_pessoas} pessoas.")
else:
    print("O arquivo JSON não contém uma lista de pessoas ou um dicionário de pessoas.")
# Criar um menu simples
def menu():
    print("Bem-vindo ao Menu de Cadastro")
    print("1. Procurar uma Pessoa")
    print("2. Cadastrar uma Pessoa")
    print("3. Editar uma Pessoa")
    print("4. Deletar uma Pessoa")
    print("5. Sair do Programa")

# Loop principal do programa
while True:
    menu()
    escolha = input("Escolha uma opção: ")
        
    if escolha == "1":
        # Lógica do menu 1
        entrada = input('Digite o nome do Cliente que procura?:')
        dados_carregados = minha_funcao()
        buscar(dados_carregados, entrada)
        
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

    elif escolha == "2":
        print('Por favor, digite as informações abaixo da pessoa a ser cadastrada:')

        nome = input('Digite o nome e sobrenome: ')
        nome = nome.split()
        idade = input('Digite a idade da pessoa: ')
        altura = input('Digite a altura da pessoa: ')
        peso = input('Digite o peso da pessoa: ')
        nascimento = input('Digite a data de nascimento (somente números): ')
        cpf = input('Digite o CPF da pessoa: ')
        cidade = input('Digite o nome da cidade da pessoa: ')
        email = input('Digite o email da pessoa: ')

        cadastro_funsão.cadastro(dados_lidos, nome, idade, altura, peso, nascimento, cpf, cidade, email)
        print('Pessoa cadastrada com sucesso!')

    elif escolha == "3":
        pass
    elif escolha == "4":
        pass
    elif escolha == "5":
        pass
    elif escolha == "6":
        break
    else:
        print("Escolha uma das opções acima.")
