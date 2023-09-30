
Rent = float(input("entre com o valor do salário:"))
print(Rent)

def calculaRent(Valor):
    print("a função foi chamada e o valor é", Valor)
    if Valor < 1250.00 : 
        print("o valor tem menos de 1250 e está recebendo aumento de 10%")
        print(Valor * 1.10)
        return Valor * 1.10
    else:
        print("o valor tem mais de 1250 e está recebendo aumento de 15%")
        # print(f"[{Rent}] = [{Valor}] * 1.15")
        print(Valor * 1.15)
        return Valor * 1.15
        

Rent = calculaRent(Rent)        
        
# print(f"o valor do Rent após o autmento foi:", Rent)


class client():
    def __init__(self, cpf, nome):
        self.nome = nome
        self.cpf = cpf
