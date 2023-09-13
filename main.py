#calculadora

#funções
import os

def clscon():
    os.system("cls" if os.name == "nt" else "clear")

def add(x, y):
    return x + y

def sub(x, y):
    if x < y:
        return y - x
    else:
        return x - y

def mut(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero ou número inválido!"

#painel
print("\nCalculadora Python\n")

while True:
    print("Selecione a Operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Fechar")

    op = input("Digite a Opção: ")

    if op == "5":
        print("\nCalculadora Finalizada.")
        break

    if op in ("1", "2", "3", "4"):
        x = float(input("\nDigite o Numero 1: "))
        y = float(input("Digite o Numero 2: "))

        if op == "1":
            resultado = add(x, y)
            print("\n", x, " + ", y, " = ", resultado)
        elif op == "2":
            resultado = sub(x, y)
            print("\n", x, " - ", y, " = ", resultado)
        elif op == "3":
            resultado = mut(x, y)
            print("\n", x, " * ", y, " = ", resultado)
        elif op == "4":
            resultado = div(x, y)
            print("\n", x, " / ", y, " = ", resultado)
    else:
        print("\nOpção inválida. Tente novamente.\n")

    input("Pressione Enter para continuar...")
    clscon()
