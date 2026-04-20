class Historico:
    def __init__(self):
        self._operacoes = []

    def adicionar_operacao(self, tipo, valor):
        self._operacoes.append(f"{tipo} de R$ {valor}")

    def listar(self):
        for op in self._operacoes:
            print(op)
