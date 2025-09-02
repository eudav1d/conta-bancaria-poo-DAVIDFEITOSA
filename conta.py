# Definindo a classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular):    
        self.titular = titular
        self.saldo = 0

    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")

if __name__ == "__main__":
    minha_conta = ContaBancaria("David Feitosa")
    print("Exibindo saldo da conta...")
    minha_conta.exibir_saldo()