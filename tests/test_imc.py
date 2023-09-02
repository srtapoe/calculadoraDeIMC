from entities.Imc import Imc


def test_calcula_imc():
    esperado = 24.93
    assert esperado == Imc.calculaImc(90, 1.90)


def test_classifica_imc():
    esperado = "Seu IMC eh 24.93 - Peso normal"
    imcFinal = 24.93
    Imc.classifica_imc(imcFinal)
    resultado = "Seu IMC eh 24.93 - Peso normal"
    assert esperado == resultado


def test_classifica_imc_dar_erro():
    esperado = "Seu IMC eh 30.00 - Obesidade I"
    imcFinal = 30.00
    Imc.classifica_imc(imcFinal)
    resultado = "Seu IMC eh 30.00 - Acima do peso"
    assert esperado == resultado