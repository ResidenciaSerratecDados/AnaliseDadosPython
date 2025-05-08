class ContaCorrente:
    def __init__(self, senha, numConta, saldo = 0.0):
        self.numConta = numConta
        self.saldo = saldo
        self.senha = senha
        
    def consultar_saldo(self):
        print(f'O saldo da conta {self.numConta}: R$ {self.saldo:.2f}')#exibir 2 casas decimais
        
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado com sucesso!\nO saldo atual da conta 1: {self.saldo:.2f}')
        else:
            print('Saldo insuficiente ou inválido!')
            
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito realizado com sucesso.\nO saldo atual da conta 1: {self.saldo:.2f}")
        else:
            print('Operação inválida.')
            
    def transferir(self, destinatario, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor
            print(f'Transferência realizada com sucesso!\nO saldo atual da conta: {self.saldo:.2f}')
        else:
            print('Saldo insuficiente ou inválido!')
        
        