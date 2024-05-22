def calcular_imc(peso, altura):
    return peso / (altura ** 2)
def main():
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.2}.")
        if imc < 18.5:
            print("Você está abaixo do peso. ")
        elif 18.5 <= imc < 24.9:
            print("Você está com peso normal. ")
        elif 25 <= imc < 29.0:
            print("Você está com sobrepeso. ")
        else:
            print("Você está com obesidade. ")
    except ValueError:
            print("Por favor, insira valores válidos para peso e altura ")
if __name__ == "__name__":
     main()              