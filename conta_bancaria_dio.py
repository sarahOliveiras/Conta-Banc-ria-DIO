""" sistema bancário com opção de depósito, saque e extrado
DEPÓSITO: valores positívos e são armazenados em uma variável
    que será exibida no extrato
SAQUE:permitido 3 saques diário com limite de 500 reais por saque.
    caso não haja saldo, o sistema dá uma mensagem de erro
    os saques são armazenados em variável e será exibido em estrato
EXTRATO:listagem de todas as operações feitas no dia. ao final
    informar o saldo em conta. valores exibidos usando R$xxx.xx
"""

qtde_depositos=0
qtde_saque = 3
saldo = 0
extrato = ""

menu = """
****CONTA BANCÁRIA****

    1)Saque
    2)Extrato/Saldo
    3)Depósito
    4)Sair
=> """


while True:
    opcao = int(input(menu))

    if opcao == 1:

        if qtde_saque == 0:
            print("Você excedeu sua quantidade de saques por dia")

        else:
            saque = float(input("Insira o valor de saque:"))

            if saque <= saldo and saque <= 500 and saque >0:
                saldo-=saque
                qtde_saque-=1
                print("Saque concluído com sucesso")
                extrato += f"Saque: R${saque:.2f}\n"

            elif saque <= 0:
                print("Coloque valores positivos e maiores que zero, tente novamente")

            else:
                print("Retire valores menores que 500 reais ou disponíveis no saldo")

    elif opcao == 2:
        texto = f"""
SEU EXTRATO

Qtde de depósitos feitos: {qtde_depositos}

Qtde de saques disponíveis: {qtde_saque}

Seu saldo atual é de: {saldo:.2f}"""
        print(texto.upper())
        print(extrato.upper())

    elif opcao == 3:
        deposito = float(input("Insira o valor de deposito:"))

        if deposito <= 0:
            print("Transação não aprovada, insira valores positivos")

        else:
            saldo+=deposito
            qtde_depositos+=1
            print("Deposito concluído com sucesso")
            extrato += f"Depósito: R${deposito:.2f}\n"

    elif opcao == 4:
        break

    else:
        print("Operação inválida, redigite")
    
