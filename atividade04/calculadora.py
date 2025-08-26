while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            if numero2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = numero1 / numero2
        else:
            raise Exception()
        print(f"O resultado é: {resultado}")
        break
        
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except Exception:
        print("Erro: Operação inválida. Por favor, insira uma operação válida (+, -, *, /).")