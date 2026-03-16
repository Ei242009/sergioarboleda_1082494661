def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobre peso"
    else:
        return "Obesidad"

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)
    print(f"Tu IMC es {imc} y tu clasificacion es: {clasificacion}")

if __name__ == "__main__":
    main()
