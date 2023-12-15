def verifie_numero(numero):
    match = re.search(r"^\d{2}-\d{3}-\d{4}$" , numero)
    if match :
        return True
    else :
        return False
