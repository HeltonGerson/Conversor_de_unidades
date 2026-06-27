import interface

interface.boasVindas()

while True:
    interface.menuInicial()

    try:
        opcao = int(input(""))
    except ValueError:
        print("Opção inválida!")
        continue

    if opcao == 0:
        print("Encerrando...")
        break

    interface.ativacaoOperacao(opcao)
