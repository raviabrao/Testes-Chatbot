print("Calculadora Universal dos Crias\n")

opcao = input("Spelecione a operação que deseja efetuar: \n1) Soma\n2) Subtração\n3) Multiplicação\n4) Divisão\n\n")

if opcao == "1":
  num1 = input("Insira o primeiro número a seguir: ")

  num2 = input("Insira o segundo número a seguir: ")

  num1 = int(num1)

  num2 = int(num2)

  print(f"A soma dos números selecionados é equivalente a: {num1 + num2}")

elif opcao == "2":
    num1 = input("Insira o primeiro número a seguir: ")

    num2 = input("Insira o segundo número a seguir: ")

    num1 = int(num1)

    num2 = int(num2)

    print(f"A subtração dos números selecionados é equivalente a: {num1 - num2}")

elif opcao == "3":

     num1 = input("Insira o primeiro número a seguir: ")

     num2 = input("Insira o segundo número a seguir: ")

     num1 = int(num1)

     num2 = int(num2)

     print(f"A multiplicação dos numeros selecionados é equivalente a: {num1 * num2}")

elif opcao == "4":

     num1 = input("Insira o primeiro número a seguir: ")

     num2 = input("Insira o segundo número a seguir: ")

     num1 = int(num1)

     num2 = int(num2)

     print(f"A divisão dos números selecionados é equivalente a: {num1 / num2}")

else:
     print("Resposta inválida, tente novamente")