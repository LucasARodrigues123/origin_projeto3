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

def cadastro(lista, nome, idade, altura, peso, nascimento, cpf, cidade, email):
    nova_pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Altura": altura,
        "Peso": peso,
        "Cidade": cidade,
        "Nascimento": nascimento,
        "CPF": cpf,
        "Email": email
    }
    lista.append(nova_pessoa)
    
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)