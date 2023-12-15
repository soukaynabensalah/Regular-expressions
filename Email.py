
def verifie_email(email):
    match = re.search(r"^\w+@\w+\.(com|ma|org|info|ru)$" , email)
    if match :
        return True
    else :
        return False
