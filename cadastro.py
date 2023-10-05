import json


# Definir o banco de dados JSON
banco_de_dados = {
    "Pessoa": [
        {
            "nome": "Lucas",
            "idade": 24,
            "peso": 58,
            "altura": 1.70,
            "nascimento": "30/05/1999",
            "cpf": "135.140.21",
            "email": "esscur11dao@gmail.com"
        }
    ]
}


# Salvar o banco de dados JSON em um arquivo
with open("banco_de_dados.json", "w") as arquivo_json:
    json.dump(banco_de_dados, arquivo_json)

# Criar um menu simples
def menu():
    print("Bem-vindo ao Menu de Cadastro")
    print("1. Listar Pessoas")
    print("2. Cadastrar uma Pessoa")
    print("3. Editar uma Pessoa")
    print("4. Procurar uma Pessoa")
    print("5. Deletar uma Pessoa")
    print("6. Sair do Programa")

# Loop principal do programa
while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        # Lógica para listar pessoas
        pass
    elif escolha == "2":
        # Lógica para cadastrar uma pessoa
        pass
    elif escolha == "3":
        # Lógica para editar uma pessoa
        pass
    elif escolha == "4":
        # Lógica para procurar uma pessoa
        pass
    elif escolha == "5":
        # Lógica para deletar uma pessoa
        pass
    elif escolha == "6":
        # Lógica para sair do programa
        break
    else:
        print("Escolha uma das opções acima.")

        
   


    