def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = f'[0-9]{{2}} [0-9]{{5}}-[0-9]{{4}}'  # Formato esperado: "XX XXXXX-XXXX"
