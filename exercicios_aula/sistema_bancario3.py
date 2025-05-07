#conta1 = {'conta1': 125489,'saldo1': 19870}#1
#conta2 = {'conta2': 547839,'saldo2': 7521}#2
saldo1 = 19870
saldo2 = 1480

while True:
    print('\n1-Consultar Saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
    op= int(input('\nEscolha uma opção: '))
    
    if op == 1:
       print(f'O saldo da conta 1: {saldo1}')
    elif op == 2:
       valor = float(input('Escolha o valor do depósito: '))
       saldo1 += valor
       print("Depósito realizado com sucesso.\nO saldo atual da conta 1: " + str(saldo1))
    elif op == 3:
       valor = float(input('Escolha o valor da transferência: '))
       saldo1 -= valor
       saldo2 += valor
       print(f'Transferência realizada com sucesso!\nO saldo atual da conta 1: {saldo1}')
    elif op == 4:
       valor = float(input('Escolha o valor do saque: '))
       saldo1 -= valor
       print(f'Saque realizado com sucesso!\nO saldo atual da conta 1: {saldo1}')
    elif op == 5:
        print('Obrigado!!!')
        break
    
def exibir_menu():
    print('\n1-Consultar Saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
    
def sacar(valor):
    global saldo
    saldo -= valor
    print(f'Saque realizado com sucesso!\nO saldo atual da conta 1: {saldo}')
    
def depositar(valor):
    global saldo
    saldo += valor
    print("Depósito realizado com sucesso.\nO saldo atual da conta 1: " + str(saldo))
    
def transferir(valor):
    global saldo, destinatario
    saldo -= valor
    destinatario += valor
    print(f'Transferência realizada com sucesso!\nO saldo atual da conta: {saldo}')
    