menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
valor = 0
saldo = 0
limite_diario = 1500
extrato = ""
limite_por_saque = 500
numero_saques = 0
limite_saques = 3
total_saques = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito concluído com sucesso!")

        else:
            print("Falha! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques < limite_saques:
            valor = float(input("Informe o valor do saque: "))
            if valor > limite_diario or valor > saldo or total_saques > limite_diario + 1 or valor > limite_por_saque:
                print(" Saque não autorizado! ")
    
            else:    
                saldo -= valor
                extrato += f"""Saque: R${valor:.2f}\n"""
                numero_saques += 1
                total_saques += valor
                print(f"Valor retirado: R${valor:.2f}")
        else:
            print("Limite de saques excedido!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigada por usar os nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")