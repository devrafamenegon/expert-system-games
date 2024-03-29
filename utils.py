def indique_genero():
    return input("Informe um gênero: ")


def indique_grau():
    return int(input("Informe o quanto você gosta desse gênero (0 a 10): "))


def deseja_adicionar_genero():
    respondeu = False

    while not respondeu:
        continuar = input("\nDeseja adicionar outro gênero? [S] ou [N]: ").lower()

        if continuar == "s":
            respondeu = True
            return True

        if continuar == "n":
            respondeu = True
            return False

        print("\nOpção inválida.")
