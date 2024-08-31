def inverter_string(s):
    string_invertida = ''
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

# Exemplo de uso
texto = "Exemplo de texto"
texto_invertido = inverter_string(texto)
print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
