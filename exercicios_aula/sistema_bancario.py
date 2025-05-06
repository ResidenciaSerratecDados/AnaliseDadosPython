# 1 - Criar lógica que verifica saldo e uma conta corrente
# - conta1, saldo

class ContaBancaria:
    def __main__(self, numero_conta, titular, saldo=0, limite=1000):
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

conta1 = ContaBancaria(numero_conta='12548-9',titular='Carlos Drumond de Andrade',saldo=19870)
conta2 = ContaBancaria(numero_conta='54783-9',titular='Fernando Pessoa',saldo=7521)

conta1.ver_saldo() #1
print('\n')
conta2.ver_saldo() #2
print('\n')
conta1.depositar(1808) #2
print('\n')
conta1.sacar(2300) #2
print('\n')
conta1.transferir(conta2, 1520) #2
print('\n')
conta1.ver_saldo() #2
print('\n')
conta2.ver_saldo() #2

# 3 - Criar um menú que permite ao usuário realizar N transações até que ele opte por sair.
# - utilizar while como menú