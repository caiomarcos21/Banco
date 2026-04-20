Sistema Bancário em Python (POO)

Este projeto é um sistema bancário simples desenvolvido em Python, utilizando **Programação Orientada a Objetos (POO)**.  
Ele foi criado como exercício acadêmico para praticar os conceitos de classes, herança, polimorfismo, agregação, composição, encapsulamento e uso de pacotes.

Funcionalidades

O sistema permite:

- Criar contas bancárias (corrente ou poupança)
- Associar um cliente a cada conta
- Depositar dinheiro em uma conta
- Sacar dinheiro de uma conta (respeitando regras de saldo e limite)
- Consultar o saldo de uma conta
- Listar o histórico de operações (depósitos e saques)
- Interagir via menu de texto no terminal

#Conceitos de POO Utilizados

- Pacotes e Módulos
  - Organização em pastas: banco/,contas/, clientes/, operacoes/ e main.py.

- Classes e Objetos
  - Cliente, Conta, ContaCorrente, ContaPoupanca, Historico, Banco.

- Herança
  - ContaCorrente e ContaPoupanca herdam de Conta.

- Polimorfismo
  - Sobrescrita do método sacar() em ContaCorrente e ContaPoupanca, com regras diferentes para cada tipo de conta.

- Agregação
  - A classe Banco mantém uma lista de contas e oferece métodos para adicioná-las e buscá-las.

- Composição
  - Cada Conta possui um objeto Historico, que registra as operações.  
    O histórico só existe enquanto a conta existir.

- Encapsulamento
  - Atributos importantes são privados (por exemplo, __saldo, __numero, __cliente, __historico)  
    e acessados por métodos como get_saldo() e get_numero().

