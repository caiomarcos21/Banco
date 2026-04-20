from operacoes.historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo_inicial = 0):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = saldo_inicial
        self.__historico = Historico()


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.adicionar_operacao("Deposito", valor)
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.adicionar_operacao("Saque", valor)
            print("Saque realizado com sucesso.")
        else:
            print("Saldo realizado com sucesso.")
    def get_saldo(self):
        return self.__saldo
    
    def mostrar_historico(self):
        self.__historico.listar()

    def get_numero(self):
        return self.__numero

    def get_cliente(self):
        return self.__cliente