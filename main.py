import interface


def main():
    interface.boasVindas()

    while True:
        interface.menuInicial()

        try:
            opcao = int(input("Escolha uma das opções acima: "))
        except ValueError:
            print("Escolha uma opção válida!!")
            continue

        if opcao == 0:
            print("Encerrando...")
            break

        interface.ativacao(opcao)


if __name__ == "__main__":
    main()

