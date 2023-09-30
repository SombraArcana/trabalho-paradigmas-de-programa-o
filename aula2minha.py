# numeros = []
# numeros_pares = []
# numeros_impare = []
# soma_pares = 0

# def main():
#     while True:
#         a = int(input("entre com os numeros desejados:"))
#         print(f"numeros restantes {9 - len(numeros)}")
#         if len(numeros) >= 10 :
#             break
#         numeros.append(a)
        
#     for x in numeros:
#         comparativo = x%2
#         if comparativo == 0:
#             numeros_pares.append(x)
#         else:
#             numeros_impare.append(x)
            
#     soma_pares = sum(numeros_pares)
#     print(f"a lista de números entrados é {numeros}\n cotendo os números pares:{numeros_pares} com a soma de: {soma_pares}\n e numeros impares:{numeros_impare}.\n o maior número do vetor é:{max(numeros)}\n e o menor numero do vetor é:{min(numeros)}")
    
            



# if __name__ == "__main__":
#     main()

import random
# cartela = []

# def gerar_cartelo():
#     numeros = set()
    
# def randomnumber():
#     return random.randint(1,100)
    
# def gerar_cartela():
#     done = []
#     for y in range(5):
#         linha = []
#         for x in range(5):
#             numero = randomnumber()
#             while numero in done:
#                 print("houve um numero repetido")
#                 numero = randomnumber()
#             linha.append(numero)
#             done.append(numero)
#         cartela.append(linha)

# gerar_cartela()
# for x in cartela:
#     print(x)

def main():
    agenda = {}
    
    while True:
        cpf = input("insira o CPF:")
        nome = input("insira o Nome:")
        idade = input("insira o idade:")
        telefone = input("insira o telefone:")
        
        agenda[cpf] = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
        }
        continuar = input("deseja continuar? (s/n):")
        if continuar != "s":
            break
        
    for cpf, contato in agenda.items():
        print(cpf,contato["nome"],contato["idade"],contato["telefone"])
    
if __name__ == "__main__":
    main()
    