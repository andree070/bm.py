primeiro_numero_inteiro = int(input("Digite o primeiro numero inteiro: "))
segundo_numero_inteiro = int(input("Digite o segundo numero inteiro: "))
numero_real = float(input("Digite o numero real: "))

produto = 2 * primeiro_numero_inteiro * 0.5 * segundo_numero_inteiro
soma = 3 * primeiro_numero_inteiro + numero_real
cubo = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo e: {produto:.2f}")
print(f"A soma do triplo do primeiro com o terceiro e: {soma:.2f}")
print(f"O terceiro elevado ao cubo e: {cubo:.2f}")
