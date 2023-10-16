import json
import cadastro_funsão

# funsoes
dados_lidos = (cadastro_funsão)
procurar_pessoa = (cadastro_funsão)
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
        if dados_lidos:
            busca = input("Digite o nome ou sobrenome que procura: ")
            resultados = procurar_pessoa(dados_lidos, busca)
            if resultados:
                for pessoa in resultados:
                    print(f' "Nome": nome,
        "Idade": idade,
        "Altura": altura,
        "Peso": peso,
        "Cidade": cidade,
        "Nascimento": nascimento,
        "CPF": cpf,
        "Email": email')
            else:
                print("Nenhuma pessoa foi encontrada com esse nome ou sobrenome")

    elif escolha == "2":
        print('Por favor, digite as informações abaixo da pessoa a ser cadastrada:')

        nome = input('Digite o nome e sobrenome: ')
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

            
    


    