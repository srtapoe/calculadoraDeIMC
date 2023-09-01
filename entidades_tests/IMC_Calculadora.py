alturaConvertida = 1.90
peso = 90.0


def calcula_imc():
    imcFinal = peso / pow(alturaConvertida, 2)
    classifica_imc(imcFinal)


def classifica_imc(imcFinal):
    if 17 > imcFinal:
        print(f"Seu IMC é: {imcFinal:.2f} - Muito abaixo do peso")
    elif 17 <= imcFinal <= 18.49:
        print(f"Seu IMC eh: {imcFinal:.2f} - Abaixo do peso")
    elif 18.49 < imcFinal <= 24.99:
        print(f"Seu IMC eh: {imcFinal:.2f} - Peso normal")
    elif 24.99 < imcFinal <= 29.99:
        print(f"Seu IMC eh: {imcFinal:.2f} - Acima do peso")
    elif 29.99 < imcFinal <= 34.99:
        print(f"Seu IMC eh: {imcFinal:.2f} - Obesidade I")
    elif 34.99 < imcFinal <= 39.99:
        print(f"Seu IMC eh: {imcFinal:.2f} - Obesidade II")
    else:
        print(f"Seu IMC eh: {imcFinal:.2f} - Obesidade III (morbida)")


calcula_imc()
