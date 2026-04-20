class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print("Conta adicionada ao banco.")

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.get_numero() == numero:
                return conta
        return None