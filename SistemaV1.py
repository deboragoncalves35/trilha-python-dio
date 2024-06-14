menu = '''
[d] = Deposito
[s] = Saque
[e] = Extrato
[q] = Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        dep = float(input('Digite o valor do depósito: '))
        saldo += dep
        extrato += 'Deposito ' + str(dep) + '\n'

    elif opcao == 's':
        saq = float(input('Digite o valor do saque: '))

        if saq > saldo:
            print('Saldo insuficiente. SAQUE NÃO AUTORIZADO')
            print(f'Saldo: {saldo:.2f}')
        elif saq > 500:
            print('Saque limitado a R$500.00. SAQUE NÃO AUTORIZADO')
        else:
            if saq <= saldo and saq <= 500:
                if numero_saques >= 3:
                    print('Limite de saques excedido (3 vezes ao dia). SAQUE NÃO AUTORIZADO')
                else:
                    saldo -= saq
                    numero_saques += 1
                    extrato += 'Saque ' + str(saq) + '\n'
                    print(f'Você tem {3 - numero_saques} saques disponíveis hoje')
      
    elif opcao == 'e':
        print(extrato)

    elif opcao == 'q':
        break
    else:
        print('Opcão Invalida. Por favor digite uma das opções acima')

print(f'{saldo:.2f}')