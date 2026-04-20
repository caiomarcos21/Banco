class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def mostrar_dados(self):
        print(f"Cliente: {self.__nome} - CPF: {self.__cpf} - Endereço: {self.__endereco}")