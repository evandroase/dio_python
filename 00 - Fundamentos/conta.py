menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)
        if opcao == "d":
            # Efetua depósito e atualiza saldo e extrato
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == "s":
            # Efetua saque e atualiza saldo, extrato e numero de saques diários
            saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "e":
            # Exibe o extrato da conta
            extrato_conta(saldo, extrato)
        elif opcao == "q":
            # Encerra o programa
            print("Encerrando o programa.")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def deposito(saldo, extrato):
    """    
    Deposita um valor positivo na conta do usuário. 
    todas as operações de depósito devem ser armazenadas no extrato.

    Args:
        saldo (float):    Saldo da conta.
        extrato (string): Extrato da conta no formato R$ XXXX.XX.
    """
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
    except ValueError:
        print("Valor de depósito inválido.")

    return saldo, extrato

def saque(saldo, extrato, num_saques, max_saques=3, limite_saque=500):
    """
    Efetua um saque na conta do usuário. Cada operação de saque tem um valor limite e também é
    possível fazer apenas um número limitado de saques por dia.

    Args:
        saldo (float):                Saldo da conta.
        extrato (string):             Extrato da conta no formato R$ XXXX.XX.
        num_saques(int)               Número de saques no dia.
        max_saques (int, optional):   Número máximo de saques diários. Limite padrão = 3.
        limite_saque (int, optional): limite da operação de saque.  Valor padrão = 500.
    """
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print(f"Saldo insuficiente. Saldo R$ {saldo:.2f}")
        elif valor > limite_saque:
            print(f"Limite excedido. Limite atual por operação R${limite_saque:.2f}")
        elif num_saques >= max_saques:
            print(f"Número de saques diários excedido. Número atual de saques por dia {num_saques}")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques += 1
    except ValueError:
        print("Valor de saque inválido")
    
    return saldo, extrato, num_saques

def extrato_conta(saldo, extrato):
    """ 
    Lista todas as operações de saque e depósito, além de mostrar o saldo ao final.
    Os valores devem aparecer no formato R$ XXXX.XX
    """
    print("\n*******************EXTRATO*******************")
    print("Nenhuma operação realizada" if extrato == "" else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("*********************************************")
    


if __name__ == '__main__':
    main()





