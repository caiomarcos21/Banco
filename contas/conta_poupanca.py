from contas.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo_inicial=0):
        super().__init__(numero, cliente, saldo_inicial)

    def sacar(self, valor):
        saldo_disponivel = self.get_saldo() 

        if 0 < valor <= saldo_disponivel:
            super().sacar(valor)  
        else:
            print("Saldo insuficiente ou valor inválido.")