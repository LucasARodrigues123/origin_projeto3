import json

try:
    with open("dados.json", 'r',) as arquivo:
        dados_lidos = json.load(arquivo)
        numero_de_pessoas = len(dados_lidos)
        print(f"Número de objetos no banco de dados: {numero_de_pessoas}")
except FileNotFoundError:
    print("O arquivo 'banco_de_dados.json' não foi encontrado.")

def minha_funsao():
    with open('dados.jon',"r") as jon:
        funsao = json.load(jon)
        return funsao
    
def procurar_pessoa():
    for busca in minha_funsao:
        


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
        # Lógica para procurar pessoa
        pass

    elif escolha == "2":
        # Lógica para cadastrar uma pessoa
        pass
    elif escolha == "3":
        # Lógica para editar uma pessoa
        pass
    elif escolha == "4":
        pass
        # Lógica para procurar uma pessoa
        # # cadastro = sorted(, key=lambda pessoa: pessoa['Nome'])
        # for pessoa in cadastro:
        #     print(f'Nome:{pessoa["Nome"]},')
    elif escolha == "5":
        # Lógica para deletar uma pessoa
        pass
    elif escolha == "6":
        # Lógica para sair do programa
        break
    else:
        print("Escolha uma das opções acima.")

        
   


    