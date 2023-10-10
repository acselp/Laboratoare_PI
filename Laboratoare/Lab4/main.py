
import random



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

# def guess_game():
#
#     # Primul jucator
#     while True:
#         numar_secret = int(input("Dati un numar secret: "))
#         if numar_secret >= 0 <= 1000:
#             break
#         else:
#             print("Eroare: Dati un numar din intervalul [0, 1000]")
#
#     if numar_secret > 100:
#         interval = [0, 1000]
#         nincercari = 10
#     else:
#         interval = [0, 100]
#         nincercari = 7
#
#     print("Jocul a inceput. Incercati sa ghiciti numarul")
#     print("Numarul se afla in intervalul", interval, "respectiv\naveti", nincercari, "incercari pentru a ghici numarul.")
#
#     auxn = nincercari
#
#     # Ciclul principal
#     while True:
#
#         guess = int(input("\nNumarul ghicit: "))
#         nincercari -= 1
#         if nincercari == 0:
#             print("Din pacate numarul de incercari a fost epuizat. \nAti perdut :(")
#             break
#         elif guess == numar_secret:
#             print("Numarul a fost ghicit.\n Felicitari!!!")
#             print("Ati ghicit numarul din", auxn - nincercari, "incercari.")
#             break
#         elif guess > numar_secret:
#             print("Trebuie mai mic!!!")
#         elif guess < numar_secret:
#             print("Trebuie mai mare!!!")
#         print("Au ramas", nincercari, "incercari. \nIncercati din nou.")
#
#
#
# guess_game()



# 3. foarfece - piatra hartie--------------------------------------------------------------------------

# def pfh():
#
#     while True:
#         print("Alegeti una din optiunile \n 1. Piatra \n 2. Hartie \n 3. Foarfece \n")
#
#         # Utilizatorul introduce una din cele 3 actiuni
#         choice = int(input("   >>> "))
#
#         # Se cere repetat de introdus daca nu a fost introdus corect
#         while choice > 3 or choice < 1:
#             choice = int(input("introduceti cifra valida din intervalul [1 - 3]: "))
#
#         # Inlocuim cifra introdusa cu denumirea actiunii corespunzatoare
#         if choice == 1:
#             choice_name = 'Piatra'
#         elif choice == 2:
#             choice_name = 'Hartie'
#         else:
#             choice_name = 'Foarfece'
#
#         print("Utilizatorul a ales: " + choice_name)
#         print("\nAcum e randul calculatorului.......")
#
#         # Pentru calculator se ia o valoare aleatoare
#         comp_choice = random.randint(1, 3)
#
#         # Inlocuim cifra introdusa cu denumirea actiunii corespunzatoare
#         # deja pentru calculator
#         if comp_choice == 1:
#             comp_choice_name = 'Piatra'
#         elif comp_choice == 2:
#             comp_choice_name = 'Hartie'
#         else:
#             comp_choice_name = 'Foarfece'
#
#         print("Calculatoru a ales: " + comp_choice_name + "\n")
#
#         print(choice_name + " V/s " + comp_choice_name + "\n")
#
#         # conditia pentru castig
#         if choice == comp_choice:
#             print("Egalitate => ")
#             result = "Egalitate"
#         elif ((choice == 1 and comp_choice == 2) or
#                 (choice == 2 and comp_choice == 1)):
#             print("Haria castigat => ")
#             result = "Hartie"
#         elif ((choice == 1 and comp_choice == 3) or
#               (choice == 3 and comp_choice == 1)):
#             print("Piatra a castigat =>")
#             result = "Piatra"
#         else:
#             print("Foarfecele au castigat =>")
#             result = "Foarfece"
#
#         # Se printeaza castigatorul
#         if result == 'Egalitate':
#             print(">>> Egalitate <<<")
#         elif result == choice_name:
#             print("\n>>> A castigat utilizatorul <<<\n")
#         else:
#             print(">>> A castigat calculatorul <<<")
#
#         print("Doriti sa jucati din nou? (y/n)")
#         ans = input()
#
#         # Conditia pentru a continua/opri jocul
#         if ans == 'n' or ans == 'N':
#             break
#
#     print("\nJocul a fost terminal.")
#
#
# pfh()


# ------------------------------------------------------------------------
#
# def pfh_avansat():
#
#     while True:
#         print('Doriti sa jucati singleplayer sau multiplayer\n 1. Singleplayer\n 2. Multiplayer')
#         q = int(input('   >>> '))
#         while 2 > q < 1:
#             q = int(input('Introduceti 1 sau 2: '))
#
#         if q == 1:
#             print('Ati ales singleplayer')
#
#
#             print("Alegeti una din optiunile\n 1. Piatra\n 2. Hartie\n 3. Foarfece\n 4. Soparla\n 5. Spock\n")
#
#             # Utilizatorul introduce una din cele 5 actiuni
#             choice = int(input("   >>> "))
#
#             # Se cere repetat de introdus daca nu a fost introdus corect
#             while choice > 5 or choice < 1:
#                 choice = int(input("introduceti cifra valida din intervalul [1 - 5]: "))
#
#             # Inlocuim cifra introdusa cu denumirea actiunii corespunzatoare
#             if choice == 1:
#                 choice_name = 'Piatra'
#             elif choice == 2:
#                 choice_name = 'Hartie'
#             elif choice == 3:
#                 choice_name = 'Foarfece'
#             elif choice == 4:
#                 choice_name = 'Soparla'
#             else:
#                 choice_name = 'Spock'
#
#             print("Utilizatorul a ales: " + choice_name)
#             print("\nAcum e randul calculatorului.......")
#
#             # Pentru calculator se ia o valoare aleatoare
#             comp_choice = random.randint(1, 5)
#
#             # Inlocuim cifra introdusa cu denumirea actiunii corespunzatoare
#             # deja pentru calculator
#             if comp_choice == 1:
#                 comp_choice_name = 'Piatra'
#             elif comp_choice == 2:
#                 comp_choice_name = 'Hartie'
#             elif comp_choice == 3:
#                 comp_choice_name = 'Foarfece'
#             elif comp_choice == 4:
#                 comp_choice_name = 'Soparla'
#             else:
#                 comp_choice_name = 'Spock'
#
#             print("Calculatoru a ales: " + comp_choice_name + "\n")
#
#             print(choice_name + " V/s " + comp_choice_name + "\n")
#             print('comp=',comp_choice, 'user=',choice)
#             # conditia pentru castig
#             result = ''
#             if choice == comp_choice:
#                 print("Egalitate => ")
#                 result = "Egalitate"
#             elif choice == 1:
#                 if (comp_choice == 3) or (comp_choice == 4):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 2:
#                 if (comp_choice == 1) or (comp_choice == 5):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 3:
#                 if (comp_choice == 2) or (comp_choice == 4):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 4:
#                 if (comp_choice == 2) or (comp_choice == 5):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 5:
#                 if comp_choice == 1 or 3:
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#
#             # Se printeaza castigatorul
#             if result == 'Egalitate':
#                 print(">>> Egalitate <<<")
#             elif result == choice_name:
#                 print("\n>>> A castigat utilizatorul <<<\n")
#             else:
#                 print(">>> A castigat calculatorul <<<")
#
#
#             print("\n\nDoriti sa jucati din nou? (y/n)")
#             ans = input()
#
#             # Conditia pentru a continua/opri jocul
#             if ans == 'n' or ans == 'N':
#                 break
#         else:
#             print('Ati ales multiplayer')
#
#             print("Primul jucator:\nAlegeti una din optiunile\n 1. Piatra\n 2. Hartie\n 3. Foarfece\n 4. Soparla\n 5. Spock\n")
#
#             # Utilizatorul introduce una din cele 5 actiuni
#             choice = int(input("   >>> "))
#
#             # Se cere repetat de introdus daca nu a fost introdus corect
#             while choice > 5 or choice < 1:
#                 choice = int(input("introduceti cifra valida din intervalul [1 - 5]: "))
#
#             # Inlocuim cifra introdusa cu denumirea actiunii corespunzatoare
#             if choice == 1:
#                 choice_name = 'Piatra'
#             elif choice == 2:
#                 choice_name = 'Hartie'
#             elif choice == 3:
#                 choice_name = 'Foarfece'
#             elif choice == 4:
#                 choice_name = 'Soparla'
#             else:
#                 choice_name = 'Spock'
#
#             print("Jucatorul 1 a ales: " + choice_name)
#             print("\nAl doilea jucator:\nAlegeti una din optiunile\n 1. Piatra\n 2. Hartie\n 3. Foarfece\n 4. Soparla\n 5. Spock\n")
#
#             # Pentru calculator se ia o valoare aleatoare
#             comp_choice = int(input("   >>> "))
#             while comp_choice > 5 or comp_choice < 1:
#                 comp_choice = int(input("introduceti cifra valida din intervalul [1 - 5]: "))
#
#             # Inlocuim cifra introdusa cu denumirea actiunii corespunzatoare
#             # deja pentru calculator
#             if comp_choice == 1:
#                 comp_choice_name = 'Piatra'
#             elif comp_choice == 2:
#                 comp_choice_name = 'Hartie'
#             elif comp_choice == 3:
#                 comp_choice_name = 'Foarfece'
#             elif comp_choice == 4:
#                 comp_choice_name = 'Soparla'
#             else:
#                 comp_choice_name = 'Spock'
#
#             print("Jucatorul 2 a ales: " + comp_choice_name + "\n")
#
#             print(choice_name + " V/s " + comp_choice_name + "\n")
#             # conditia pentru castig
#             result = ''
#             if choice == comp_choice:
#                 print("Egalitate => ")
#                 result = "Egalitate"
#             elif choice == 1:
#                 if (comp_choice == 3) or (comp_choice == 4):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 2:
#                 if (comp_choice == 1) or (comp_choice == 5):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 3:
#                 if (comp_choice == 2) or (comp_choice == 4):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 4:
#                 if (comp_choice == 2) or (comp_choice == 5):
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#             elif choice == 5:
#                 if comp_choice == 1 or 3:
#                     print(choice_name + ' a castigat =>')
#                     result = choice_name
#                 else:
#                     print(comp_choice_name + ' a castigat =>')
#                     result = comp_choice_name
#
#             # Se printeaza castigatorul
#             if result == 'Egalitate':
#                 print(">>> Egalitate <<<")
#             elif result == choice_name:
#                 print("\n>>> A castigat jucatorul 1 <<<\n")
#             else:
#                 print(">>> A castigat jucatorul 2 <<<")
#
#             print("\n\nDoriti sa jucati din nou? (y/n)")
#             ans = input()
#
#             # Conditia pentru a continua/opri jocul
#             if ans == 'n' or ans == 'N':
#                 break
#
#     print("\nJocul a fost terminal.")
#
#
# pfh_avansat()


# -----------------------------------------------------------------------------------------
#
# def cap_pajura():
#     while True:
#         print('\n\nAlegeti:\n 1. Cap\n 2. Pajura\n 3. Iesire')
#         q = int(input('\n   >>> '))
#
#         if q == 3:
#             break
#
#         res = random.randint(1, 2)
#
#         if q == res:
#             print('\nAti castigat!!!')
#         else:
#             print('\nAti pierdut :(')
#
# cap_pajura()



# ----------------------------------------------------------



def paiul_mai_scurt():

    while True:

        print('\n\nAlegeti un pai de la 1 la trei (`0 pentru a iesi`):')
        q = int(input('\n   >>> '))
        while q < 0 > 3:
            q = int(input('\nIncercati din nou:'))

        if q == 0:
            break

        res = random.randint(1, 3)

        if q == res:
            print('\nAti pierdut :(')
        else:
            print('\nAti castigat!!!')

paiul_mai_scurt()