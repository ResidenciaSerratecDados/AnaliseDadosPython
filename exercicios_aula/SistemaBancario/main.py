#cd C:\AnaliseDadosPython\exercicios_aula\SistemaBancario
# python main.py para rodar no terminal

from conta import ContaCorrente

conta1 = ContaCorrente('1234-5',100.00)
conta2 = ContaCorrente('9876-5',2000.00)

def exibir_menu():
    print('\n1-Consultar Saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')

while True:
    exibir_menu()
    op= int(input('\nEscolha uma opção: '))
    
    if op == 1:
       conta1.consultar_saldo()
    elif op == 2:
       valor = float(input('Escolha o valor do depósito: '))
       conta1.depositar(valor)
    elif op == 3:
       valor = float(input('Escolha o valor da transferência: '))
       conta1.transferir(conta2, valor)
    elif op == 4:
       valor = float(input('Escolha o valor do saque: '))
       conta1.sacar(valor)
    elif op == 5:
        print('Obrigado!!!')
        break
    else:
        print('\nOpção inválida. Tente novamente\n')