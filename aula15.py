# AULA 15

class ContaCorrente:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"Saldo da conta corrente: R${self._saldo}")


class Poupanca(ContaCorrente):
    def exibir_saldo(self):
        print(f"Saldo da poupança: R${self._saldo}")


class ContaImposto(ContaCorrente):
    def __init__(self, saldo, percentualImposto):
        super().__init__(saldo)
        self._percentualImposto = percentualImposto

    @property
    def percentualImposto(self):
        return self._percentualImposto

    @percentualImposto.setter
    def percentualImposto(self, valor):
        if valor < 0 or valor > 1:
            raise ValueError("O percentual do imposto deve ser entre 0 e 1")
        self._percentualImposto = valor

    def calcularImposto(self):
        self._saldo -= self._saldo * self._percentualImposto

    def exibir_saldo(self):
        print(f"Saldo da conta imposto: R${self._saldo}")

conta_corrente = ContaCorrente(1000)
conta_corrente.depositar(500)
conta_corrente.sacar(200)
conta_corrente.exibir_saldo()

poupanca = Poupanca(2000)
poupanca.depositar(500)
poupanca.sacar(200)
poupanca.exibir_saldo()

conta_imposto = ContaImposto(3000, 0.15)
conta_imposto.depositar(500)
conta_imposto.sacar(200)
conta_imposto.calcularImposto()
conta_imposto.exibir_saldo()

# Prof. perdão pelos erros, usei a IA para entender pois não pude participar da aula
