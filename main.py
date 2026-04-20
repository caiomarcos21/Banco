from clientes.cliente import Cliente
from banco.banco import Banco
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

from clientes.cliente import Cliente
from banco.banco import Banco
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca


def mostrar_menu():
    print("\n=== MENU BANCO ===")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Consultar Saldo")
    print("5 - Histórico")
    print("0 - Sair")


if __name__ == "__main__":
    banco = Banco("Banco Caio")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break

        elif opcao == "1":
            print("\n--- Criar Conta ---")
            numero = int(input("Número da conta: "))
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            endereco = input("Endereço do cliente: ")

            cliente = Cliente(nome, cpf, endereco)

            print("Tipo de conta:")
            print("1 - Corrente")
            print("2 - Poupança")
            tipo = input("Escolha o tipo (1 ou 2): ")

            if tipo == "1":
                limite = float(input("Limite da conta corrente: "))
                conta = ContaCorrente(numero, cliente, 0, limite)
            elif tipo == "2":
                conta = ContaPoupanca(numero, cliente, 0)
            else:
                print("Tipo de conta inválido.")
                continue

            banco.adicionar_conta(conta)
            print("Conta criada com sucesso!")

        elif opcao == "2":
            print("\n--- Depositar ---")
            numero = int(input("Número da conta: "))
            conta = banco.buscar_conta(numero)

            if conta is None:
                print("Conta não encontrada.")
            else:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)

        elif opcao == "3":
            print("\n--- Sacar ---")
            numero = int(input("Número da conta: "))
            conta = banco.buscar_conta(numero)

            if conta is None:
                print("Conta não encontrada.")
            else:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)

        elif opcao == "4":
            print("\n--- Consultar Saldo ---")
            numero = int(input("Número da conta: "))
            conta = banco.buscar_conta(numero)

            if conta is None:
                print("Conta não encontrada.")
            else:
                print("Saldo atual:", conta.get_saldo())

        elif opcao == "5":
            print("\n--- Histórico ---")
            numero = int(input("Número da conta: "))
            conta = banco.buscar_conta(numero)

            if conta is None:
                print("Conta não encontrada.")
            else:
                conta.mostrar_historico()

        else:
            print("Opção inválida. Tente novamente.")