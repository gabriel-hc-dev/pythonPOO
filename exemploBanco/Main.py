class Main:
    pass 

print("App de Controle Bancário")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Daniel", "18987623434")
conta = Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()

print("Nome do Titular: ", conta.titular, "\nNúmero do Titular: ", conta.numero, "\nSaldo: ", conta.saldo)