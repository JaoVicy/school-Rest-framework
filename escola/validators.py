import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = f'[0-9]{{2}} [0-9]{{5}}-[0-9]{{4}}'  # Formato esperado: "XX XXXXX-XXXX"
    resposta = re.fullmatch(modelo, celular)
    return not resposta