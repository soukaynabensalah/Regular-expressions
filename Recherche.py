import re
def recherche(mot, chaine):
    pattern = re.escape(mot)
    match = re.search(pattern, chaine)
    if match :
        return True
    else :
        return False
    
