conta1 = {'conta1': 125489,'saldo1': 19870}#1
conta2 = {'conta2': 547839,'saldo2': 7521}#2

while True:
    op= int(input('\nEscolha uma opção: '))
    
    if op == 1:
       
    elif op == 2:
        
    elif op == 3:
        
    elif op == 4:
        
    elif op == 5:
        print('Obrigado!!!')
        break
    
def exibir_menu():
    print('\n1-Consultar Saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
    
def sacar(valor):
    global saldo
    saldo -= valor
    print("Saque de " + str(valor) + " realizado com sucesso. Saldo: " + str(saldo))
    
def depositar(valor):
    global saldo
    saldo += valor
    print("Depósito de " + str(valor) + " realizado com sucesso. Saldo: " + str(saldo))
    
def transferir(valor):
    global saldo, destinatario
    saldo -= valor
    destinatario += valor
    print(f'Transferência realizada com sucesso!\nO saldo atual da conta: {saldo}')