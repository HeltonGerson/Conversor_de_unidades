import config
import engine


def boasVindas():
    print("Seja bem vindo!\ndigite [ENTER] para continuar...")
    input("")


def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(f"{mensagem}"))
            return valor
        except ValueError:
            print("Digite um valor válido!!")
            continue


def ler_unidade(dicionario):

    while True:
        origem = input("")
        if origem not in dicionario:
            print("Digite uma unidade válida!!")
            continue

        destino = input("")
        if destino not in dicionario:
            print("Digite uma unidade válida!!")
            continue

        return origem, destino


def menuInicial():
    print("O que deseja converter?")
    print("1. Moeda")
    print("2. Unidades de medidas")
    print("0. Sair")


def ativacao(opcao):
    if opcao == 1:
        valor = operacaoMoeda()
        return print(f"{valor:.2f}")
    if opcao == 2:
        return menuMedidas()
    return print("Digite uma opção válida!!")


def operacaoMoeda():
    print("Escolha duas das moedas abaixo: ")

    for i in config.unidade_monetaria:
        print(i)

    origem, destino = ler_unidade(config.unidade_monetaria)

    valor = ler_valor("Digite um valor a ser convertido: ")

    return engine.conversaoUnidades(
        valor, config.unidade_monetaria[origem], config.unidade_monetaria[destino]
    )


def ler_opcao(mensagem):
    while True:
        try:
            opcao = int(input(f"{mensagem}"))
            return opcao
        except ValueError:
            print("Escolha uma opção válida!!")
            continue


def menuMedidas():
    print("Qual medida deseja operar: \n")
    print("1. Comprimento\n2. temperatura\n3. tempo\n4. massa")

    return ativacaoMenuMedidas()


def ativacaoMenuMedidas():

    while True:
        opcao = ler_opcao("Digite uma das opções acima: ")

        if opcao not in [1, 2, 3, 4]:
            print("Escolha uma opção válida!!")
            continue

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
    for i in config.unidade_comprimento:
        print(i)

    origem, destino = ler_unidade(config.unidade_comprimento)
    valor = ler_valor("Digite um valor a ser convertido: ")

    return engine.conversaoUnidades(
        valor, config.unidade_comprimento[origem], config.unidade_comprimento[destino]
    )


def temperatura():
    print("Escolha uma das unidades abaixo: ")
    print("C", "F", "K")

    while True:
        origem = input("Digite a origem").upper()
        destino = input("Digite o destino").upper()

        if (origem, destino) not in config.unidade_temperatura:
            print("Escolha unidades válidas!!")
            continue

        valor = ler_valor("Digite um valor a ser convertido: ")

        unidades_escolhidas = config.unidade_temperatura[(origem, destino)]
        resultado = unidades_escolhidas(valor)

        return resultado


def tempo():
    print("Escolha uma das unidades abaixo: ")
    for i in config.unidade_tempo:
        print(i)

    origem, destino = ler_unidade(config.unidade_tempo)
    valor = ler_valor("Digite um valor a ser convertido: ")

    return engine.conversaoUnidades(
        valor, config.unidade_tempo[origem], config.unidade_tempo[destino]
    )


def massa():
    print("Escolha uma das unidades abaixo: ")
    for i in config.unidade_massa:
        print(i)

    origem, destino = ler_unidade(config.unidade_massa)
    valor = ler_valor("Digite um valor a ser convertido: ")

    return engine.conversaoUnidades(
        valor, config.unidade_massa[origem], config.unidade_massa[destino]
    )
