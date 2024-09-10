def inverter_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Testando a função
string = "exemplo"
print(f"String invertida: {inverter_string(string)}")
