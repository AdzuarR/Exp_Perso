def str_superieur_a_n_caractere(string,nombre):
    """Retourne vrai si password plus grand que nombres
    param password, chaine de caractere
    param nombre, entier representant une taille de chaine de caractere
    return res, booleen, par defaut a False
    """
    res = False
    if nombre != None:
        if len(string)>nombre:
            res = True
    return res

assert not str_superieur_a_n_caractere(None,None)
assert not str_superieur_a_n_caractere("abcdef",7)
assert str_superieur_a_n_caractere("abcdefghij",7)
    
def contient_plus_de_n_chiffres(password,nombre):
    """
    Fonction qui renvoi vrai si password contient plus de nombres chiffres
    param password, chaine de caractere
    param nombre, entier representant le nombre de chiffres a depasser
    return res, booleen, par defaut a False
    """
    res = False
    if nombre != None:
        compteur = 0
        ind = 0
        while not res and ind < len(password):
            #compteur contient le nombre de chiffres du mot de passe compris entre
            # password[0] a password[ind-1]
            if password[ind].isnumeric():
                compteur+=1
            ind+=1
            if compteur > nombre:
                res = True
    return res

assert not contient_plus_de_n_chiffres(None,None)    
assert not contient_plus_de_n_chiffres("abcd",0)    
assert contient_plus_de_n_chiffres("abcd9",0)    

def contient_aucun_espace(password):
    """
    Fonction qui renvoi vrai si le password ne contient pas d'espace
    param password, chaine de caractere
    return res, booleen par defaut a True
    """
    ind = 0
    res = True
    while ind < len(password) and res:
        #invariant: password ne contient pas d'espace entre la valeur
        # password[0] a password[ind-1]
        if password[ind]==" ":
            res = False
        ind +=1
    return res

assert contient_aucun_espace("")
assert not contient_aucun_espace(" ")
assert not contient_aucun_espace(" abcd")
assert contient_aucun_espace("abcde")

def contient_une_majuscule(password):
    """
    Fonction qui retourne vrai si le mot de passe contient une majuscule
    param password, chaine de caractere
    return res, booleen par defaut a False
    """
    res = False
    ind = 0
    while ind < len(password) and not res:
        #Password ne contient pas de majuscule entre les valeurs
        # password[0] et password[ind-1]
        if password[ind].isupper():
            res = True
        ind += 1
    return res

assert not contient_une_majuscule("")
assert not contient_une_majuscule("abcd")
assert contient_une_majuscule("abcD")

def pas_deux_majuscules_consecutive(password):
    """
    Fonction qui renvoi vrai si le mot de passe ne contient pas deux majuscules consecutive
    param password, chaine de caractere
    return res, booleen par default a True
    """
    res = True
    ind = 1
    while ind < len(password) and res and len(password)>1:
        #password ne contient pas deux majuscules consecutive entre
        #password[0] et password[ind-1]
        if password[ind-1].isupper() and password[ind].isupper():
            res = False
        ind +=1
    return res

assert pas_deux_majuscules_consecutive("")
assert pas_deux_majuscules_consecutive("AbCd")
assert not pas_deux_majuscules_consecutive("ABCd")
assert not pas_deux_majuscules_consecutive("ABC")

def pas_de_caractere_speciaux(password):
    """
    Fonction qui retourne vrai si la chaine ne contient pas de caractere special
    param password, chaine de caractere
    return res, booleen par default a True
    """
    res = True
    ind = 0
    while ind < len(password) and res:
        #password ne contient pas de caractere speciaux entre
        # password[0] et password[ind-1]
        if not password[ind].isalnum():
            res = False
        ind += 1
    return res

assert pas_de_caractere_speciaux("")
assert pas_de_caractere_speciaux("abcd")
assert not pas_de_caractere_speciaux("abcd*")
assert not pas_de_caractere_speciaux("?abcd")

# Programme principal

def dialogueMotDePasse():
    nombre_minimum_de_caractere = 8
    nombre_minimum_de_chiffres = 1
    password = input("Entrer votre mot de passe : ")

    valid = False
    while not valid:
        if str_superieur_a_n_caractere(password,nombre_minimum_de_caractere-1):
            if contient_plus_de_n_chiffres(password,nombre_minimum_de_chiffres-1):
                if contient_aucun_espace(password):
                    if contient_une_majuscule(password):
                        if pas_deux_majuscules_consecutive(password):
                            if pas_de_caractere_speciaux(password):
                                valid = True
                            else:
                                print("Le mot de passe ne doit pas contenir de caractere speciaux")
                        else:
                            print("Le mot de passe ne doit pas contenir plusieurs majuscules consecutives")
                    else:
                        print("Le mot de passe doit contenir au moins une majuscule")
                else:
                    print("Le mot de passe ne doit pas contenir d'espaces")
            else: # str contient_plus_de_n_chiffres est faux
                print("Le mot de passe doit contenir au moins "+str(nombre_minimum_de_chiffres)+" chiffres")
        else: # str_superieur_a_n est faux
            print("Le mot de passe doit contenir plus de "+str(nombre_minimum_de_caractere)+" caracteres")
        
        
        if valid:
            fic = open("mdpUltrasecret.txt",'w')
            fic.write(password)
            fic.close()
        else:
            password = input("Entrer votre mot de passe : ")

dialogueMotDePasse()
