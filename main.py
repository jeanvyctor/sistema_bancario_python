saldo = 0
extrato = ''
limite_saque = 500
numero_de_saques = 0
LIMITE_SAQUES = 3

print( ''' 
----------------------
BEM VINDO AO SEU BANCO
---------------------- 

[!] SELECIONE A OPÇÃO QUE DESEJA REALIZAR:''')

while True:

    menu = int(input( '''
    [1] VER EXTRATO
    [2] DEPOSITAR 
    [3] SACAR
    [4] SAIR
    => 
    '''))

    if menu == 2:
        valor_depositar = float(input('''Insira o valor: R$ '''))
        if valor_depositar > 0:
            saldo += valor_depositar
            extrato += f'Depósito         R$ {valor_depositar:.2f}\n'
            print("Seu depósito foi realizado com sucesso!")
        else:
            print("Valor inválido. Tente novamente!")
        

    elif menu == 3:
        if numero_de_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido. Tente novamente mais tarde!")
        else: 
            valor_sacar = float(input("Digite o valor que deseja sacar: R$"))
            if valor_sacar > saldo:
                print('Seu saldo é insuficiente para realizar essa transação.')
            elif valor_sacar > limite_saque:
                print("O valor solicitado excede o limite de R$500 por saque.")
            elif valor_sacar <= 0:
                print("Valor solicitado inválido. Tente novamente!")
            else:
                saldo -= valor_sacar
                numero_de_saques += 1
                extrato += f'Saque            R$ {valor_sacar:.2f}\n'
                print("Saque realizado com sucesso!")
    
    elif menu == 1:
        print("\n=========== EXTRATO ===========")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual:    R$ {saldo:.2f}")
        print("================================")

    elif menu == 4:
        print('''
        ==================================    
        Obrigado por utilizar nosso banco
        ==================================
                  VOLTE SEMPRE!
                                      ''')
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4. ")
