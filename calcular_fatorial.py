# Algoritimo para calcular o fatorial de um número

# Função para calcular o fatorial

def calcular_fatorial(numero):
    if numero == 0:
        return
    else:
        return numero * calcular_fatorial (numero - 1)
    
# Receber o número do usuário

numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é positivo

if numero < 0:
    print("Erro: O número deve ser positivo.")
else:
    # Calcular e exibir o fatorial
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)