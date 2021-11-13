
import random
import string

# 1.--------------------------------------------------------------
print("\n 1. ")

# Introducere suma a doua cifre de la tastatura cu verificarea erorilor
def _1():
    while True:
        try:
            # Incercam sa introducem
            a = int(input("  a = "))
            b = int(input("  b = "))
            print("  a + b =", a + b)
            break
        except:
            # Daca apar careva exceptii sau erori se va afisa urmatorul mesaj
            # Apoi va avea loc urmatoarea iteratie
            print("  Nu ati introdus un numar intreg.\nIncercati din nou")


_1()

# 2.------------------------------------------------
# Lista imbricata
l = [[1, 2, [3, 4]], [5, 6], 7]
print("\n 2. ")

# Functia care liniarizeaza lista
def _2(l):
    for i in l:
        if not isinstance(i, int):
            yield from _2(i)
        else:
            yield i


print(l)
print("  ", list(_2(l)))

# 3.---------------------------------------------------
print(" 3.-----------------------------------------------")
# Gaseste toate cuvintele anagrame din lista

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

l = ['ACEST', 'ASCET', 'CAR', 'IEPURE', 'CASET', 'CASTE', 'CESTA', 'ALBUM', 'MARCEL']
a = []

for word1 in l:
    for word2 in l:
        if(word1 == word2):
            continue
        if(a.__contains__(word1) and a.__contains__(word2)):
            continue
        if isAnagram(word1, word2):
            if(a.__contains__(word1)):
                a.append(word2)
            elif(a.__contains__(word2)):
                a.append(word1)
            else:
                a.append(word2)
                a.append(word1)
print(l)
print("In lista data au fost gasite urmatoarele anagrame:\n")
print(a)

# 4.---------------------------------------------------
# Dictionarul
d = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}
print("\n 4. ")

# Functia care interschimba cheile
def _4(d):
    # Extragem cheile si valorile in liste diferite
    keys = list(d.keys())
    values = list(d.values())

    #
    for i in range(len(keys)):
        d[values[i]] = keys[i] # Cream un element cu cheia si valoarea inversata
        d.pop(keys[i]) # Stergem cheia veche
    print("  ", d)


_4(d)

# 5.-----------------------------------------------------
# Doua liste cu lungimi egale
a = [1, 5, 8, 6, 4, 7, 8, 9, 5]
b = [5, 7, 8, 7, 4, 6, 1, 8, 7]

print("\n 5. ")

# Produsul unei liste
def prod(l):
    p = 1
    for i in l:
        p *= i
    return p

# Suma produselor listelor
def _5_1(a, b):
    if len(a) != len(b):
        raise Exception("Liste cu lungimi diferite")
    else:
        return prod(a) + prod(b)

# Suma produselor fiecarui element din ambele liste
def _5_2(a, b):
    if len(a) != len(b):
        raise Exception("Liste cu lungimi diferite")
    else:
        s = 0
        for i in range(len(a)):
            s += a[i] * b[i]
    return s


print("  5_1. ", _5_1(a, b))
print("  5_2. ", _5_2(a, b))

# 6.------------------------------------------------------------

print("\n 6. ")
# Tuplurile date
brendan = ("Brendan", "McCane")
sandy = ("Sandy", "Garner")
nick = ("Nick", "Meek")
student1 = ("Allan", "Anderson")
student2 = ("Barry", "Byars")
student3 = ("Christine", "Carver")
student4 = ("Delia", "de Wattinger")

# -----------------------------------------

# (a) Pune tuplele într-o listă, apoi utilizați un ciclu pentru a afișa doar fiecare prenume.
print("a)")
l = [brendan, sandy, nick, student1, student2, student3, student4]
for i in l:
    print(i[1]) # Printam elementul de pe poz 1 (al doilea element) din fiecare tuplu, aflat in lista

# (b) Atribuie toate numele unei variabile de tip set numit Visio.
print("b)")
Visio = [i[0] for i in l] # Folosind List comprehansion punem in Visio primul element din fiecare tuplu
print(Visio)

# (c) Atribuie primele 3 tupluri unei variabile de tip set numit profesori.
print("c)")
profesori = l[:3] # Folosind Slicing tool atribuim unei liste primele trei elemente (tupluri)
print(profesori)

# (d) Atribuie restul la o variabilă set numit studenți.
print("d)")
studenti = l[3:] # Folosind Slicing tool atribuim unei liste restul elementelor, adica elementele incepand cu indexul 3
print(studenti)

# (e) utilizează for pentru a imprima numele fiecărui elev, de exemplu corect formatat
print("e)")
for i in studenti:
    print(i[0], i[1])

# (f) Utilizați un ciclu pentru a imprima numele fiecărui profesor folosind doar prima literă a prenumelui de ex B.
print("f)")
ch = "S"
for i in profesori:
    if i[0][0] == ch:
        print(i[1])

# 7. Facem un dictionar cu toate cuvintele din text si numarul lor de aparitie
# Citeste continutul fisierului si il atribuie unei variabile
print("7. ---------------------------------------")
f = open("file.txt", "r", encoding="utf-8")
s = f.read()
f.close()

# Folosim metoda split() pentru a separa cuvintele
l = s.split()
d = {}

for word in l:
    if not d.__contains__(word): # Astfel initialiam un element pentru a putea in continuare sa il incrementam
        d[word] = 1
    else:
        d[word] += 1

# Dictionarul nu este un tip de date ordonat, sau care poate fi parcurs ca o liista simpla
# De aceea pentru a sorta dictionarul dupa valori cream un dictionar nou, unde vom plasa
# deja elementele in ordine crescatoare
d2 = {}
# Extragem valorile si cheile din dictionar pentru a putea parcurge si sorta valorile acestuia
keys = list(d.keys())
values = list(d.values())

ind = 0
max = 0
# Selection sort pentru dictionare
for i in range(len(d)):
    for j in range(len(d)):
        if d2.__contains__(keys[j]):
            continue
        if max < values[j]:
            max = values[j]
            ind = j

    d2[keys[ind]] = max # Adaugam in alt dictionar elementele in ordine descrescatoare
    max = 0

print("\n")
for item in d2.items():
    print(item)

# 8.-------------------------------------------------
str = "Programul va crea și va afișa pe ecran un dicționar în care vor fi stocate cuvintele și numărul de apariții ale acestora în textul din fișier. Îmbunătățește programul prin imprimarea cuvintele în ordinea descrescătoare a numărului de apariții."
# Stergem spatiile goale din sirul de caractere
str = str.replace(" ", "")
l = []

# Facem o lista care contine sirul de caractere separat in cate 3 caractere
for i in range(2, len(str), 3): # Ciclu cu pasul de 3
    l.append(str[i - 2] + str[i - 1] + str[i]) # Concatenam cate 3 caractere din sir

# Schimbam din fiecare element caracterul din mijloc cu unul aleator
for index, fragment in enumerate(l):
    q = 1
    while q == 1:
        rand_chr = random.choice(string.ascii_letters)
        if rand_chr in fragment: # Verifica daca sirul nu contine acel caracter care urmeaza a fi introdus
            continue
        else:
            new_frag = fragment[0] + rand_chr + fragment[2]
            l[index] = new_frag
            q = 0

print("8. ---------------------------------------------")
print(l)

# 9.------------------------------------------------------------------
# Dictionarul
d = {
    1: 2,
    2: 2,
    5: 9,
    7: 5,
    9: 1
}

# Extragem elementele din dictionar pentru a putea opera cu ele in continuare
l = list(d.items())
print("9. ---------------------------------------------")
print(d)
# Verifica fiecare element cu fiecare element daca cheia primului este mai mare decat
# valoare celui deal doilea
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][0] > l[j][1]: # Daca a fost gasit un astfel de element el va fi sters
            d.pop(l[i][0])
            break
print(d)

