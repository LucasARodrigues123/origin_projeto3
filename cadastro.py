import json
import cadastro_funsão


client = "lucas"
idade = 24
altura = 1.70
peso = 58
nascimento = "30/05/1999"
cpf = "13510225721"
cidade = "curitiba"
email = "lucas@gmail.com"

# Criando um dicionário
dados = {
    "Client": client,
    "Idade": idade,
    "Altura": altura,
    "Peso": peso,
    "Nascimento": nascimento,
    "Cpf": cpf,
    "Cidade": cidade,
    "Email": email
}

# Salvando o dicionário em um arquivo JSON
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo ,indent=4)

     

# funsoes
dados_lidos = (cadastro_funsão)
procurar_pessoa = (cadastro_funsão)
# Criar um menu simples
carregar_dados_json =(cadastro_funsão)
print(carregar_dados_json)
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
        if dados_lidos:
            busca = input("Digite o nome ou sobrenome que procura: ")
            resultados = procurar_pessoa(dados_lidos, busca)
            if resultados:
                for pessoa in resultados:
                    print(f' "Nome"')
        
            else:
                print("Nenhuma pessoa foi encontrada com esse nome ou sobrenome")

    elif escolha == "2":
        print('Por favor, digite as informações abaixo da pessoa a ser cadastrada:')

        nome = input('Digite o nome e sobrenome: ')
        nome = nome.split
        idade = input('Digite a idade da pessoa: ')
        altura = input('Digite a altura da pessoa: ')
        peso = input('Digite o peso da pessoa: ')
        nascimento = input('Digite a data de nascimento (somente números): ')
        cpf = input('Digite o CPF da pessoa: ')
        cidade = input('Digite o nome da cidade da pessoa: ')
        email = input('Digite o email da pessoa: ')

        cadastro(nome, idade, altura, peso, nascimento, cpf, cidade, email)
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

            
    


    