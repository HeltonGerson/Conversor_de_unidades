import os

import config
import engine


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def desenhar_caixa(linhas, titulo=None, largura=40):
    interno = largura - 2
    if titulo is None:
        topo = "┌" + "─" * interno + "┐"
    else:
        conteudo_topo = "── " + titulo + " "
        topo = "┌" + conteudo_topo + "─" * (interno - len(conteudo_topo)) + "┐"

    corpo = ["│" + linha.ljust(interno) + "│" for linha in linhas]
    base = "└" + "─" * interno + "┘"

    print("\n".join([topo, *corpo, base]))


def pausar(mensagem="  Digite [ENTER] para voltar ao menu..."):
    input(mensagem)


def mostrar_resultado(texto):
    desenhar_caixa([texto], titulo="Resultado")
    pausar()


def boasVindas():
    limpar_tela()
    desenhar_caixa(
        [
            "CONVERSOR DE UNIDADES".center(38),
            "Seja bem-vindo!".center(38),
        ]
    )
    input("  Digite [ENTER] para continuar...")


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
        origem = input("Digite a origem: ").lower()
        if origem not in dicionario:
            print("Digite uma unidade válida!!")
            continue

        destino = input("Digite o destino: ").lower()
        if destino not in dicionario:
            print("Digite uma unidade válida!!")
            continue

        return origem, destino


def menuInicial():
    limpar_tela()
    desenhar_caixa(
        [
            "  1. Moeda",
            "  2. Unidades de medidas",
            "  0. Sair",
        ],
        titulo="O que deseja converter?",
    )


def ativacao(opcao):
    if opcao == 1:
        operacaoMoeda()
        return
    if opcao == 2:
        return menuMedidas()
    return print("Escolha uma opção válida!!")


def operacaoMoeda():
    limpar_tela()
    desenhar_caixa(
        [f"  {i}" for i in config.unidade_monetaria],
        titulo="Escolha duas das moedas abaixo",
    )

    origem, destino = ler_unidade(config.unidade_monetaria)

    valor = ler_valor("Digite um valor a ser convertido: ")

    resultado = engine.conversaoUnidades(
        valor, config.unidade_monetaria[origem], config.unidade_monetaria[destino]
    )
    mostrar_resultado(f"  {valor:.2f} {origem} = {resultado:.2f} {destino}")


def ler_opcao(mensagem):
    while True:
        try:
            opcao = int(input(f"{mensagem}"))
            return opcao
        except ValueError:
            print("Escolha uma opção válida!!")
            continue


def menuMedidas():
    limpar_tela()
    desenhar_caixa(
        [
            "  1. Comprimento",
            "  2. Temperatura",
            "  3. Tempo",
            "  4. Massa",
        ],
        titulo="Qual medida deseja operar?",
    )

    return ativacaoMenuMedidas()


def ativacaoMenuMedidas():

    while True:
        opcao = ler_opcao("Digite uma das opções acima: ")

        if opcao not in [1, 2, 3, 4]:
            print("Escolha uma opção válida!!")
            continue

        if opcao == 1:
            comprimento()
            return
        if opcao == 2:
            temperatura()
            return
        if opcao == 3:
            tempo()
            return
        if opcao == 4:
            massa()
            return


def comprimento():
    limpar_tela()
    desenhar_caixa(
        [f"  {i}" for i in config.unidade_comprimento],
        titulo="Escolha duas das unidades abaixo",
    )

    origem, destino = ler_unidade(config.unidade_comprimento)
    valor = ler_valor("Digite um valor a ser convertido: ")

    resultado = engine.conversaoUnidades(
        valor, config.unidade_comprimento[origem], config.unidade_comprimento[destino]
    )
    mostrar_resultado(f"  {valor:.2f} {origem} = {resultado:.2f} {destino}")


def temperatura():
    limpar_tela()
    desenhar_caixa(
        ["  c", "  f", "  k"],
        titulo="Escolha duas das unidades abaixo",
    )

    while True:
        origem = input("Digite a origem").lower()
        destino = input("Digite o destino").lower()

        if (origem, destino) not in config.unidade_temperatura:
            print("Digite unidades válidas!!")
            continue

        valor = ler_valor("Digite um valor a ser convertido: ")

        resultado = config.unidade_temperatura[(origem, destino)](valor)
        mostrar_resultado(f"  {valor:.2f} {origem} = {resultado:.2f} {destino}")
        return


def tempo():
    limpar_tela()
    desenhar_caixa(
        [f"  {i}" for i in config.unidade_tempo],
        titulo="Escolha duas das unidades abaixo",
    )

    origem, destino = ler_unidade(config.unidade_tempo)
    valor = ler_valor("Digite um valor a ser convertido: ")

    resultado = engine.conversaoUnidades(
        valor, config.unidade_tempo[origem], config.unidade_tempo[destino]
    )
    mostrar_resultado(f"  {valor:.2f} {origem} = {resultado:.2f} {destino}")


def massa():
    limpar_tela()
    desenhar_caixa(
        [f"  {i}" for i in config.unidade_massa],
        titulo="Escolha duas das unidades abaixo",
    )

    origem, destino = ler_unidade(config.unidade_massa)
    valor = ler_valor("Digite um valor a ser convertido: ")

    resultado = engine.conversaoUnidades(
        valor, config.unidade_massa[origem], config.unidade_massa[destino]
    )
    mostrar_resultado(f"  {valor:.2f} {origem} = {resultado:.2f} {destino}")
