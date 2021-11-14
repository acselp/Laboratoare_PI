




# 1. Mystic 8 Ball -----------------------------------------------------------
#
# import random as rand
#
# def num_prezicere(num):
#     if num == 1:
#         return "Este sigur"
#     elif num == 2:
#         return "Este incontestabil"
#     elif num == 3:
#         return "Fără îndoială"
#     elif num == 4:
#         return "Da - cu siguranţă"
#     elif num == 5:
#         return "Puteţi să vă bazaţi pe ea"
#     elif num == 6:
#         return "După cum văd eu lucrurile, da"
#     elif num == 7:
#         return "Cel mai probabil"
#     elif num == 8:
#         return "Outlook bun"
#     elif num == 9:
#         return "Punct de semne pentru a da"
#     elif num == 10:
#         return "Da"
#     elif num == 11:
#         return "Răspuns neclar, încercaţi din nou"
#     elif num == 12:
#         return "Adresaţi-vă din nou mai târziu"
#     elif num == 13:
#         return "Mai bine nu-ţi spun acum"
#     elif num == 14:
#         return "Nu se poate prezice acum"
#     elif num == 15:
#         return "Se concentrează şi întreabă din nou"
#     elif num == 16:
#         return "Nu conta pe el"
#     elif num == 17:
#         return  "Răspunsul meu este nu"
#     elif num == 18:
#         return "Sursele mele spun că nu"
#     elif num == 19:
#         return "Perspectivele nu sunt atît de bune"
#     elif num == 20:
#         return "Foarte dubios"
#
# def mystic_ball():
#     s = ""
#     while True:
#         s = input("Introduceti intrebarea: ")
#         print("Intrebarea a fost... " + s)
#         print("Se scutura bila...\nApare raspunsul...")
#         print("Bila misterioasa ne spune... " + num_prezicere(rand.randint(1, 20)) + "\n\n")
#         print("1. Incearca din nou\n0. Iesire")
#
#         q = int(input("\n    >>> "))
#         if q == 1:
#             continue
#         elif q == 2:
#             return
#         else:
#             print("Dati o valoare corecta!!!")
#             continue
#
#
# mystic_ball()
#
#


# 2. -------------------------------------------

def guess_game():

    # Primul jucator
    while True:
        numar_secret = int(input("Dati un numar secret: "))
        if numar_secret >= 0 <= 1000:
            break
        else:
            print("Eroare: Dati un numar din intervalul [0, 1000]")

    if numar_secret > 100:
        interval = [0, 1000]
        nincercari = 10
    else:
        interval = [0, 100]
        nincercari = 7

    print("Jocul a inceput. Incercati sa ghiciti numarul")
    print("Numarul se afla in intervalul", interval, "respectiv\naveti", nincercari, "incercari pentru a ghici numarul.")

    auxn = nincercari

    # Ciclul principal
    while True:

        guess = int(input("\nNumarul ghicit: "))
        nincercari -= 1
        if nincercari == 0:
            print("Din pacate numarul de incercari a fost epuizat. \nAti perdut :(")
            break
        elif guess == numar_secret:
            print("Numarul a fost ghicit.\n Felicitari!!!")
            print("Ati ghicit numarul din", auxn - nincercari, "incercari.")
            break
        elif guess > numar_secret:
            print("Trebuie mai mic!!!")
        elif guess < numar_secret:
            print("Trebuie mai mare!!!")
        print("Au ramas", nincercari, "incercari. \nIncercati din nou.")



guess_game()



