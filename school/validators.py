def valid_cpf(cpf_number):
    return len(cpf_number) == 11

def valid_name(name):
    return name.isalpha()

def valid_rg(rg_number):
    return len(rg_number) == 9