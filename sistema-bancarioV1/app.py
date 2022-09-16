from operator import truediv
from os import system
from time import sleep
system('clear')

menu_banco = '''
    [ 1 ] - Depositar
    [ 2 ] - Sacar
    [ 3 ] - Ver o extrato
    [ 4 ] - Sair

    => Escolha a operação desejada: 
'''
saldo = 0
limite = 1000
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem vindo ao DIO Bank")
sleep(1.5)

while True:

    opcao = input(menu_banco)

    if opcao == '1':
        valor_deposito = float(input('Informe o valor do depósito: '))

        if valor_deposito > 0:
            saldo += valor_deposito 
            extrato += f'Depósito feito no valor de R$ {valor_deposito:.2f}'
        else:
            print('Valor inválido, tente novamente!')

    elif opcao == '2':
        valor_saque = float(input('Informe o valor a sacar: '))

        EXCEDEU_SALDO = valor_saque > saldo
        EXCEDEU_LIMITE = valor_saque > limite
        EXCEDEU_SAQUES = numero_saques >= LIMITE_SAQUES

        if EXCEDEU_SALDO:
            print("Saldo insuficiente para este saque")
        elif EXCEDEU_LIMITE:
            print('O valor do saque excede o limite')
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'Saque: R${valor_saque:.2f}\n'
            numero_saques += 1

        else:
            print('O valor informado é inválido. Por favor, tente novamente')
    
    elif opcao == '3':
        sleep(1.5)
        print("===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('='*19)

    elif opcao == '4':
        print('Obrigado por escolher os nossos serviços. volte sempre.')
        sleep(1)
        break

    else:
        print('Opção inválida, tente novamente.')
