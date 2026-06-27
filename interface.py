import config
import engine


def boasVindas():
    print("Seja bem vindo!\ndigite [ENTER] para continuar...")
    input("")


def menuInicial():
    print("O que deseja converter?")
    print("1. Moeda")
    print("2. Unidades de medidas")
    print("0. Sair")


def ativacaoOperacao(opcao):

    if opcao not in [1, 2, 0]:
        print("Escolha uma opção válida!!")
        return

    if opcao == 1:
        valor = operacaoMoeda()
        return print(f"{valor:.2f}")
    if opcao == 2:
        return menuMedidas()


def operacaoMoeda():
    print("Escolha duas das moedas abaixo: ")
    for i in config.unidade_monetaria:
        print(i)
    origem = input("")
    destino = input("")

    valor = float(input("Quanto deseja converter: "))

    return engine.conversaoUnidades(
        valor, config.unidade_monetaria[origem], config.unidade_monetaria[destino]
    )


def menuMedidas():
    print("Qual medida deseja operar: \n")
    print("1. Comprimento\n2. temperatura\n3. tempo\n4. massa")
    opcao = int(input(""))

    if opcao == 1:
        resultado = comprimento()
        return print(f"{resultado:.2f}")
    if opcao == 2:
        resultado = temperatura()
        return print(f"{resultado:.2f}")
    if opcao == 3:
        resultado = tempo()
        return print(f"{resultado:.2f}")
    if opcao == 4:
        resultado = massa()
        return print(f"{resultado:.2f}")


def comprimento():
    print("Escolha duas das unidades abaixo: ")
    for i in config.unidades_comprimento:
        print(i)

    origem = input("")
    destino = input("")

    valor = float(input("Quanto deseja converter: "))

    return engine.conversaoUnidades(
        valor, config.unidades_comprimento[origem], config.unidades_comprimento[destino]
    )


def temperatura():
    print("Escolha uma das unidades abaixo: ")
    print("C", "F", "K")

    origem = input("").upper()
    destino = input("").upper()

    tupla = (origem, destino)
    valor = float(input("Digite o valor que deseja converter: "))

    unidades_escolhidas = config.unidade_temperatura[tupla]
    resultado = unidades_escolhidas(valor)

    return resultado


def tempo():
    print("Escolha uma das unidades abaixo: ")
    for i in config.unidades_tempo:
        print(i)

    origem = input("")
    destino = input("")

    valor = float(input("Quanto deseja converter: "))

    return engine.conversaoUnidades(
        valor, config.unidades_tempo[origem], config.unidades_tempo[destino]
    )


def massa():

    print("Escolha uma das unidades abaixo: ")
    for i in config.unidade_massa:
        print(i)

    origem = input("")
    destino = input("")

    valor = float(input("Quanto deseja converter: "))

    return engine.conversaoUnidades(
        valor, config.unidade_massa[origem], config.unidade_massa[destino]
    )
