import interface

interface.boasVindas()

while True:
    interface.menuInicial()

    try:
        opcao = int(input("Escolha uma das opções acima: "))
    except ValueError:
        print("Digite uma opção válida!!")
        continue

    if opcao == 0:
        print("Encerrando...")
        break

    interface.ativacao(opcao)
