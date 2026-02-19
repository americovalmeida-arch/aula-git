def somar(a, b):
    return a + b 

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

#P G P

while True:
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo da Calculadora")
        break

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o 1° numero: "))
        num2 = float(input("Digite o 2° número: "))

        if opcao == "1":
            resultado = somar(num1, num2)
            print("Resultado: ", num1 + num2)

        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print("Resultado:", num1 - num2)

        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print("Resultado:", num1 * num2)

        elif opcao == "4":
            resultado = dividir(num1, num2)
            print("Resultado:", num1 / num2)
        
        else: print("Opção inválida! Tente novamente.")