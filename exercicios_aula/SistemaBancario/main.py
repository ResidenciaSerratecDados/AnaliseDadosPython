#cd C:\AnaliseDadosPython\exercicios_aula\SistemaBancario
# python main.py para rodar no terminal

from conta import ContaCorrente

contas = {
    '1234-5': ContaCorrente('132','1234-5',100.00),
    '9876-5': ContaCorrente('111','9876-5',2000.00)
}

def login():
    num_conta = input('Digite seu número da conta: ')
    senha = input('Digite sua senha: ')
    conta = contas.get(num_conta)
    
    if conta and conta.senha == senha:
        print(f'Seja bem-vindo(a), {conta.num_conta}!')
    else:
        print('Login ou Senha Inválidos.\nTente Novemente!')
    

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