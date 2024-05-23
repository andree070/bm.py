def calcular_peso_ideal(altura):
    if altura <= 0:
        raise ValueError("Altura deve ser um valor positivo: ")
    return(72.7 * altura) - 58
altura = float(input("Digite sua altura em metros: "))
peso_ideal = calcular_peso_ideal(altura)
print(f"Seu peso ideal e de aproximadamente {peso_ideal:.2f}")