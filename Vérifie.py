def verifie_chaine(chaine):
    match = re.search(r"\d" , chaine)
    if match :
        return True
    else :
        return False
    

