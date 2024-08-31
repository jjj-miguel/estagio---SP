import json

def calcular_faturamento_json(arquivo):
    with open(arquivo, 'r') as file:
        data = json.load(file)
    
    faturamento_diario = [item['valor'] for item in data['faturamento_diario'] if item['valor'] > 0]
    
    if not faturamento_diario:
        return None, None, 0
    
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

# Exemplo
menor, maior, dias_acima_media = calcular_faturamento_json('faturamento.json')

print(f"Menor valor de faturamento: R${menor}")
print(f"Maior valor de faturamento: R${maior}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
