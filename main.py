def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate printr-un singur spatiu: ")
    numbersAsString = givenString.split(" ")
    for i in numbersAsString:
        l.append(int(i))
    return l


def eliminareDuplicate(l):
    """
    functia elimina valorile duplicate din lista
    l - o lista citita de la tastatura
    return - lista fara valorile duplicate
    """
    pass


def main():
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afisare lista dupa eliminarea duplicatelor")
        print ("x. Iesire")
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            l = eliminareDuplicate(l)
            print(l)
        elif optiune == "x":
            break
        else: print("Optiune invalida!")


main()
