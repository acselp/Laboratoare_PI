# Iata un exemplu de
# rezultat a acestui program:
#
# Intrebarea a fost... Voi deveni eu bogat?
# Se scutura bila.
# Apare raspunsul...
# Bila misterioasa ne spune... Probabil da.
#
# Intrebarea a fost... Va cistiga Zimbru campionatul europei?
# Se scutura bila.
# Apare raspunsul...
# Bila misterioasa ne spune... Probabil nu.


# Pozitiv:
# ● Este sigur (fără îndoială)
# ● Este incontestabil (o concluzie dinainte)
# ● Fără îndoială (fără îndoială)
# ● Da - cu siguranţă (cu siguranta da)
# ● Puteţi să vă bazaţi pe ea (Puteţi fi sigur de asta)
#
# Ezitant pozitiv
# ● După cum văd eu lucrurile, da (cred - "da")
# ● Cel mai probabil (cel mai probabil)
# ● Outlook bun (perspective bune)
# ● Punct de semne pentru a da (semnul spune - "da")
# ● Da (Yes)
#
# Neutru
# ● Răspuns neclar, încercaţi din nou (nu este clar, încercaţi din nou)
# ● Adresaţi-vă din nou mai târziu (întrebaţi mai târziu)
# ● Mai bine nu-ţi spun acum (Mai bine nu spun)
# ● Nu se poate prezice acum (Cine nu poate prezice)
# ● Se concentrează şi întreabă din nou (concentrat şi de a pune din nou)
#
# Negativ
# ● Nu conta pe el (nu cred)
# ● Răspunsul meu este nu (Răspunsul meu - "nu")
# ● Sursele mele spun că nu (Potrivit informaţiilor mele - "nu")
# ● Perspectivele nu sunt atît de bune (Perspectivele nu sunt foarte bune)
# ● Foarte dubios (îndoielnic)


# Importa modulul random

# Scrieti o functie numar_prezice
# Aceasta va fi o funcţie ajutatoare.
# E ava primi parametru numar si va returna un sir
#
# Numerele posibile pot fi de la 1 pina la 10 inclusiv.
# fiecare numar ar trebui sa faca previziuni
# care va fi raspunsul da sau nu.
#
# Sugestii de raspuns luati de mai sus.
# 0 – Da, probabil!
# 1 – Definitiv nu.
# ...
#
# Daca se tasteaza alta cifra decit cele pina la 10
# trebuie sa afiseze ca ceva nu este corect
# mesaj de atentionare si reintroduce numarul.

# def numar_prezice(numar):
#
#
# # Scrie aici codul.
# # Utilizeaza if...elif...else
# # pentru a verifica numarul
# # si a returna sirul prezis.
#
#
# def mystical_ball(intrebarea):


# afiseaza intrebarea initiala in consola

# Afiseaza "Ai agitat bila misterioasa."

# Utilizeaza randrange pentru a afla numarul aleator

# Use functia ce transleaza
# numarul selectat aleator
# in prezicere


# Construieste suspens prin adaugind un rind nou
# Apare raspunsul


# Afiseaza un rind
# Bila ne spune...
# si introdu prezicerea


# afiseaza un rind nou



# Testeaza programul cu intrebarile

def num_prezicere(num):
    if num == 1:
        return "Este sigur (fără îndoială)"
    elif num == 2:
        return "Este incontestabil (o concluzie dinainte)"
    elif num == 3:
        return "Fără îndoială (fără îndoială)"
    elif num == 4:
        return "Da - cu siguranţă (cu siguranta da)"
    elif num == 5:
        return "Puteţi să vă bazaţi pe ea (Puteţi fi sigur de asta)"
    elif num == 6:
        return "După cum văd eu lucrurile, da (cred - 'da')"
    elif num == 7:
        return "Cel mai probabil (cel mai probabil)"
    elif num == 8:
        return "Outlook bun (perspective bune)"
    elif num == 9:
        return "Punct de semne pentru a da (semnul spune - 'da')"
    elif num == 10:
        return "Da (Yes)"
    elif num == 11:
        return "Răspuns neclar, încercaţi din nou (nu este clar, încercaţi din nou)"
    elif num == 12:
        return "Adresaţi-vă din nou mai târziu (întrebaţi mai târziu)"
    elif num == 13:
        return "Mai bine nu-ţi spun acum (Mai bine nu spun)"

    # ●
    # ●
    # ●
    # ● Nu se poate prezice acum (Cine nu poate prezice)
    # ● Se concentrează şi întreabă din nou (concentrat şi de a pune din nou)
    #
    # Negativ
    # ● Nu conta pe el (nu cred)
    # ● Răspunsul meu este nu (Răspunsul meu - "nu")
    # ● Sursele mele spun că nu (Potrivit informaţiilor mele - "nu")
    # ● Perspectivele nu sunt atît de bune (Perspectivele nu sunt foarte bune)
    # ● Foarte dubios (îndoielnic)


mystical_ball("Voi fi eu bogat?")
mystical_ball("Va cîstiga Zimbru campionatul europei?")
