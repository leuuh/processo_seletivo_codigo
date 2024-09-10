import json

dados = '''{
    "faturamento": [220.5, 0, 180.3, 0, 320.1, 100.0, 0, 50.3, 0]
}'''

faturamento = json.loads(dados)["faturamento"]

# Removendo dias sem faturamento
faturamento_filtrado = [f for f in faturamento if f > 0]

# Menor e maior valor de faturamento
menor = min(faturamento_filtrado)
maior = max(faturamento_filtrado)

# Média mensal
media = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Dias com faturamento acima da média
dias_acima_da_media = sum(1 for f in faturamento_filtrado if f > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_da_media}")
