def menu():
    menu = """\n
    ================ MENU ================
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nc]Nova conta
    [lc]Listar contas
    [nu]Novo usuário
    [q]Sair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite_diario, numero_saques, limite_por_saque, limite_saques, total_saques):
    if numero_saques < limite_saques:
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

    return saldo, extrato

def exibir_extrato(saldo, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, criação de conta encerrada!")


def listar_contas(contas):
    for conta in contas:
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        print("=" * 100)

def main():
    agencia = "0001"
    valor = 0
    saldo = 0
    limite_diario = 1500
    extrato = ""
    limite_por_saque = 500
    numero_saques = 0
    limite_saques = 3
    total_saques = 0
    usuarios=[]
    contas=[]

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)


        elif opcao == "q":
            print("Obrigada por usar os nossos serviços!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
