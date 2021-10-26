import math
from datetime import date

# -----------------------------First chapter------------------------------------


# 1. Miles into km--------------------------
def mile_km(mile):
    return (mile * 1.609344)


print("1.", mile_km(9))


# 2. Time in seconds-------------------------
def time_converter(h, m, s):
    return (h * 3600) + (m * 60) + s


print("2.", time_converter(1, 1, 1))


# 3. Square surface & perimeter---------------
def surface_perimeter(length, width):
    s = length * width  #suprafata patrulaterului
    p = (2 * length) + (2 * width)   #perimetrul
    return [s, p]


lt = 5
h = 9
square_data = surface_perimeter(lt, h)
print("3. A square with length = ", lt, " cm and height = ", h, " cm, has a surface of ", square_data[0], " and a perimeter of ", square_data[1])


# 4. Circle length and surface---------------------
def circumferinta_cerc(r):
    lt = 2 * math.pi * r    # Lungimea circumferintei
    s = math.pi * r**2    # Suprafata cercului
    return [lt, s]


print("4. length = ", circumferinta_cerc(8)[0], " surface = ", circumferinta_cerc(8)[1])


# 5. Deposit-----------------------------------------------------------------------------------
def depozit_valoare(valoare_curenta, rata_anuala, n_ani):
    total_gain = 0  # Initializam cu 0 pentru a putea efectua in continuare operatii

    for i in range(n_ani):     # Calculeaza dobanda pentru numarul de ani pentru depozitare (se repeta de "n_ani" ori)
        total_gain = total_gain + (valoare_curenta * ((rata_anuala + 100) / 100) - valoare_curenta)

    return valoare_curenta, valoare_curenta + total_gain, rata_anuala    # total_gain este dobanda castigata in anii de depozitare


print("5. Current value", depozit_valoare(100500, 8, 5)[0], ", value after depositing = ", depozit_valoare(100500, 2, 5)[1], ", year rate: ", depozit_valoare(100500, 2, 5)[2], "%")


# 6. Person age----------------------------------------------------------------
def varsta_persoana(day, month, year):
    curr_date = date.today()
    birth_date = date(year, month, day)
    age = curr_date - birth_date

    return age.days


print("6. This person is ", varsta_persoana(14, 4, 2001), " days age. He was born in ", date(1990, 8, 14))
print("------------------------First chapter finished----------------------\n\n")

# -------------------------------------Second chapter-------------------------------------


# 1. Numar par-----------
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


n = 3
a = "not" if is_even(n) else ""
print("1. Number ", n, " is ", a, " odd.")


# 2. Gaseste nume----------------------------
def gaseste_nume(name):
    if name == "Ion":
        return True
    elif name == "Elena":
        return True
    elif name == "Maria":
        return True
    else:
        return False


print("2.", gaseste_nume("Maria"))


# 3. Leap year------------------------------
def an_bisect(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


print("3.", an_bisect(2100))


# 4. Intersection interval
def intersectare_interval(a, b, c, d):
    for i in range(a, b):
        if i in range(c, d):
            return True
        else:
            return False

print("Intervalele [1, 4] si [2, 5] se intersecteaza = ", intersectare_interval(1, 4, 2, 5))

# 5. Name and age
def numele_si_varsta(name, age):
    if age < 0:
        return "Error: Invalid age!!!"
    else:
        return name + age.__str__()


print("5.", numele_si_varsta("Gingis Han, ", -5))

                                                                  
# 6. Afiseaza numere
def afiseaza_numere(n):
    if n < 0 or n >= 100:
        print("6. Error: Number out of the range: [0, 100)")
        return
    else:
        n2 = n
        u = n % 10
        n = math.trunc(n / 10)
        z = n % 10

        print("6. The number", n2, "has", z, "tenths and", u, "units")


afiseaza_numere(56)


# 7. Find names.
# Am schimbat din array de tupluri in dictionar si am folosit Try - Except
teacher_data = {
    "Vasile": "Moraru",
    "Mihail": "Perebinos",
    "Ion": "Sirghi",
    "Stefan": "Buzurniuc"
}


def find_lastname(first_name):
    try:
        print("7. For the first name:", first_name, "has been found last name:", teacher_data[first_name])
    except:
        print("7. Error: No such teacher")


find_lastname("Vasile")


# 8. Pig Latin
def is_vocala(c):  # Verifies if the parameter is a vocal
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True
    else:
        return False


def move_fst_2_end(s):  # Moves first char at the end of the string
    aux = s[0]
    s = s[1:]
    s = s + aux

    return s


def pig_latin(s):
    if is_vocala(s[0]):
        return s + "way"
    else:
        return move_fst_2_end(s) + "ay"


print("8.", pig_latin("pig"))
print("-----------------------Second chapter finished-----------------------")