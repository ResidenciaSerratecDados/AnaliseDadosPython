# 1 - Criar lógica que verifica saldo e uma conta corrente
# - conta1, saldo

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0, limite=1000):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def ver_saldo(self):
        print("Conta:", self.numero_conta)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)
        print("Limite:", self.limite)

# 2 - Criar uma segunda conta corrente para simular saque, deposito e transferência
# - conta2, saldo
# - saque, depósito e transferência

    def depositar(self, valor):       
        self.saldo += valor
        print("Depósito de " + str(valor) + " realizado com sucesso. Saldo: " + str(self.saldo))
         
    def sacar(self, valor):       
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print("Saque de " + str(valor) + " realizado com sucesso. Saldo: " + str(self.saldo))
        else:
            print("Saldo insuficiente. Tente um valor menor.")
            
    def transferir(self, destino, valor):        
        if self.saldo >= valor:
            self.sacar(valor)
            destino.depositar(valor)
            print("Transferência de " + str(valor) + " para conta " + str(destino.numero_conta) + " realizada com sucesso.")
        else:
            print("Saldo insuficiente para transferir. Tente um valor menor.")

conta1 = ContaBancaria(numero_conta=125489,titular='Carlos Drumond de Andrade',saldo=19870)#1
conta2 = ContaBancaria(numero_conta=547839,titular='Fernando Pessoa',saldo=7521)#2
#conta2.ver_saldo() #2

# 3 - Criar um menú que permite ao usuário realizar N transações até que ele opte por sair.
# - utilizar while como menú
while True:
    print('\n1-Consultar Saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
    op= int(input('\nEscolha uma opção: '))
    
    if op == 1:
        conta1.ver_saldo()
    elif op == 2:
        conta1.depositar(valor = float(input('Quanto você deseja depositar: ')))
    elif op == 3:
        conta1.transferir(conta2,valor = float(input('Quanto você deseja transferir: ')))
    elif op == 4:
        conta1.sacar(valor = float(input('Quanto você deseja sacar: ')))
    elif op == 5:
        print('Obrigado!!!')
        break