import json

data = {
    "faturamento": [
        22174.1664, 24537.6698, 26139.6134, 0.0, 0.0,
        26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722,
        0.0, 0.0, 3847.4823, 373.7838, 2659.7563,
        48924.2448, 18419.2614, 0.0, 0.0, 35240.1826,
        43829.1667, 18235.6852, 4355.0662, 13327.1025,
        0.0, 0.0, 25681.8318, 1718.1221, 13220.495,
        8414.61
    ]
}

faturamento = [dia for dia in data["faturamento"] if dia > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for dia in faturamento if dia > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")