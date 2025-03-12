novaConta = 'sim'
while novaConta == 'sim':

    num1 = float(input("Digite o primeiro número: ").replace(',', '.'))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: ").replace(',', '.'))

    if operador != '+' and operador != '-' and operador != '*' and operador != '/':
        print("Operador inválido.")
        continue
    elif operador == '+':
        resultado = num1 + num2
        print(f"o resultado da conta: {num1} {operador} {num2} = {resultado}")
    elif operador == '-':
        resultado = num1 - num2
        print(f"o resultado da conta: {num1} {operador} {num2} = {resultado}")
    elif operador == '*':
        resultado = num1 * num2
        print(f"o resultado da conta: {num1} {operador} {num2} = {resultado}")
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"o resultado da conta: {num1} {operador} {num2} = {resultado}")
        else:
            print("Divisão por zero não é permitida.")
    novaConta = input("Deseja fazer uma nova conta? (sim/não): ")
