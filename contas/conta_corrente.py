from contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo_inicial=0, limite=100):
        super().__init__(numero, cliente, saldo_inicial)
        self.__limite = limite

    def sacar(self, valor):
        saldo_disponivel = self.get_saldo() + self.__limite

        if 0 < valor <= saldo_disponivel:
            super().sacar(valor)  
        else:
            print("Saldo + limite insuficientes ou valor inválido.")