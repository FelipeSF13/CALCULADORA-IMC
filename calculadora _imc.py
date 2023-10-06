def calcular_imc(peso, altura):
    # Fórmula do IMC: peso / (altura * altura)
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 34.9 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Solicita ao usuário que insira seu peso e altura
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Interpreta o IMC
classificacao = interpretar_imc(imc)

# Exibe o resultado
print(f"Seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")
