def calcular_soma(indice):
    soma = 0
    for k in range(1, indice + 1):
        soma += k
    return soma

print(f"O valor da variável SOMA é: {calcular_soma(13)}")