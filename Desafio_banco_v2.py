


def menu():
    menu = """\n
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    => """
    return input((menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n------------------------------------------\n"
        print("\nDepósito realizado com sucesso!")
    
    else:
        print("\nO valor informado é inválido, tente novamente.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente!")

    elif excedeu_limite:
        print("\nO valor do saque excede o limite!")

    elif excedeu_saques:
        print("\nNúmero máximo de saques excedido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n------------------------------------------\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("=========================================")
    print(f"Saldo:\t\tR$ {saldo:.2f}")
    print("=========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
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
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, verifique o CPF e tente novamente!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}"""
        print("\t(Caso não esteja vendo seu usuario crie uma conta!)\n")
        print("=" * 42)
        print((linha))
        print("=" * 42)
    if not contas:
        print("\n\tNão existem contas ativas!")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    valor1 = 0
    while True:
        opcao = menu()

        if opcao == "1":
            try:
                valor1 = float(input("Informe o valor do depósito: "))
            except ValueError:
                print ("O valor informado é inválido, tente novamente.")
                continue
            valor = valor1
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            try:
                valor = float(input("\nInforme o valor do saque: "))
            except ValueError:
                print ("O valor informado é inválido, tente novamente.")
                continue
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print( "Obrigado por usar nosso caixa eletrônico!\n" )
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()