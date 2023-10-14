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
        return None

def minha_funcao():
    try:
        with open('dados.json', 'r') as arquivo:
            funcao = json.load(arquivo)
        return funcao
    except FileNotFoundError as e:
        print(f"O arquivo não foi encontrado. Erro: {e}")
        return None

# Lógica do menu 1
def procurar_pessoa(dados, termo):
    resultados = []
    termo = termo.lower()
    for pessoa in dados:
        if termo in pessoa['Nome'].lower() :
            resultados.append(pessoa)
    return resultados

dados_lidos = minha_funcao()

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
                    print(f'Nome: {pessoa["Nome"]}')
            else:
                print("Nenhuma pessoa foi encontrada com esse nome ou sobrenome")

    elif escolha == "2":
           
        pass
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

            
    


    