# 1 - Criar lógica que verifica saldo e uma conta corrente
# - conta1, saldo
conta1 = {
    'nome': 'Luan',
    'numero': '100088-5',
    'saldo': 2356.89
}

# 2 - Criar uma segunda conta corrente para simular saque, deposito e transferência
# - conta2, saldo
# - saque, depósito e transferência
conta2 = {
    'nome': 'Ely',
    'numero': '190088-7',
    'saldo': 2959.85
}
transferencia = float(input('Quanto deseja transferir?'))
saque = float(input('Quanto deseja sacar?'))
deposito = float(input('Quanto deseja depositar?'))

#2a)transferencia
saldo = saldo.conta2 - transferencia.conta1
#2b)saque
saldo = saldo.conta2 - saque.conta2
#2c)deposito
saldo = saldo.conta2 + deposito.conta1

# 3 - Criar um menú que permite ao usuário realizar N transações até que ele opte por sair.
# - utilizar while como menú