# Dados de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total de faturamento
valor_total = sum(faturamento.values())

# Calcula e exibe o percentual de representação de cada estado
percentuais = {estado: (valor / valor_total) * 100 for estado, valor in faturamento.items()}

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
