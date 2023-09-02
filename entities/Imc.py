class Imc:
    def calculaImc(peso, altura):
        peso = float(peso)
        altura = float(altura)
        imcFinal = float(peso / pow(altura, 2))
        return round(imcFinal, 2)

    def classifica_imc(imcFinal):
        if imcFinal < 17:
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
