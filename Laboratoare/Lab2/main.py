import math


# 1.----------------------------------------------------------------
# Suma numerelor impare pana la n
def suma_impare(n):
    sum = 0
    for i in range(1, n, 2):  # Range 1 : _n with step 2
        sum = sum + i
    return sum


print(" 1. ", suma_impare(10))


# 2.---------------------------------------------------------------
# Verifies if the prod if digits equals to p
def prod_verify(n, p):
    a = n % 10
    n = n // 10

    b = n % 10
    n = n // 10

    c = n % 10

    if a * b * c == p:
        return True
    else:
        return False


def prime_nums_prod(_p):
    prime = []
    res = []


    # Find the all prime numbers which are of 3 digits
    for num in range(100, 999):
        # all prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime.append(num)

    # Find all the prime numbers whose digit product equals to _p
    for n in prime:
        if prod_verify(n, _p):
            res.append(n)

    return res


print(" 2. ", prime_nums_prod(9))


# 3.--------------------------------------------------------------------
# Suma divizorilor lui n
def sum_divisors(_n):
    s = 0
    for i in range(1, _n + 1):
        if _n % i == 0:
            s = s + i
    return s


def friend_nums(a, b):
    b = b + 1
    d = {}
    res = []

    for i in range(a, b):
        d[i] = sum_divisors(i) # Dictionarul cu suma divizorilor pentru fiecare numar din intervalul [a, b]

    for i in range(a, b):
        for j in range(a, b):
            if i == j:  # Excludem elementele cu valorile tuplului identice
                continue
            elif res.__contains__((i, j)) or res.__contains__((j, i)):  # Excludem tuplurile cu elementele asemanatoare
                continue
            elif d[i] == d[j]:
                res.append((i, j))
    return res


print(" 3. ", friend_nums(10, 25))


# 4.-------------------------------------------------------------------------------------------------------

def div_com(nr, div):
    n = 0
    print(" 4. ")
    for i in range(1, nr + 1):
        for j in range(i + 1, nr + 1):
            if math.gcd(i, j) == div:
                n = n + 1
                print((i, j))
    print(n, " perechi")

div_com(20, 6)

# 5.-------------------------------------------------------------------------------------------------------


def is_consec(n):
    a = n % 10
    n = n // 10

    b = n % 10
    n = n // 10

    c = n

    if a > b > c:
        return True
    else:
        return False


def sum_digits(n):
    # Calculeaza suma cifrelor unui numar
    a = n % 10
    n = n // 10

    b = n % 10
    n = n // 10

    c = n
    return a + b + c


def sum(s):
    arr = []

    for i in range(100, 1000):
        if is_consec(i) and sum_digits(i) == s:
            arr.append(i)

    print(" 5. ", arr)


sum(18)

# 6.-------------------------------------------------------------------------------


def desc(x):
    arr = []
    prim = []
    p = 0
    i = 0

    # Numerele prime pana la x
    for num in range(2, x + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prim.append(num)
    i = 0
    p = 0
    while x > 1:
        while x % prim[i] == 0:
            p = p + 1
            x = x / prim[i]

        if p == 0:
            i = i + 1
            continue

        arr.append((prim[i], p))
        p = 0
        i = i + 1

    print(" 6. ", arr)


desc(512)

# 7.---------------------------------------------------------------------


def reverse(x):
    return int(str(x)[::-1])


i = 0
a = []


def _7():
    for i in range(10, 100):
        if i**2 == reverse(reverse(i)**2):
            a.append(i)
    print(" 7. ", a)


_7()

# 8.------------------------------------------------------------------


def _8(n):
    d = []
    r = []

    # Gasim divizorii proprii
    for i in range(1, n):
        k = 0
        for j in range(1, i):
            if(i % j == 0 and j != 1 and j != i):
                k = k + 1
        d.append((i, k))
    # Gasim numerele cu cei mai multi divizori proprii
    max = -1
    ind = 0
    for i in range(len(d)):
        if(d[i][1] >= max):
            max = d[i][1]
            ind = i
    # Numaram cate numere cu nr maxim de div proprii
    a = []
    for i in range(len(d)):
        if(d[i][1] == max):
            a.append(i)

    for i in a:
        r.append(d[i])
    print(" 8. ", r)

_8(20)

# 9.------------------------------------------------------


def _9(k):
    i = 1
    while(True):
        count = 0
        for j in range(1, i + 1):
            if(i % j == 0):
                count = count + 1
        if(count == k):
            print(" 9. ", i)
            break
        i = i + 1

_9(4)


# 10.---------------------------------------------------

k = 0


def is_prime(x):
    global k
    if x == 2:
        return True
    for i in range(2, x):
        if(x % i == 0):
            return False
        elif(i == x - 1):
            return True


r = []


def _10():
    prime = []
    r = []

    # generam numere prime
    for num in range(100, 999):

        for i in range(2, num):
            if(num % i == 0):
                break
            elif(i == num - 1):
                prime.append(num)

    # verificam care numere sunt inverse si prime
    for num in prime:
        if(is_prime(reverse(num))):
            if(not r.__contains__((num, reverse(num))) and not r.__contains__((reverse(num), num)) and reverse(num) != num):
                r.append((num, reverse(num)))

    print(" 10. ", r)

_10()

# 11.--------------------------------------------------------------------------------------------------------------------
#   Numere perfecte
def _11(x):
    s = 0

    for i in range(1, x):
        if(x % i == 0):
            s = s + i

    if(s == x):
        print(" 11.  Numarul", x, "este pefect. Suma divizorilor este:", s)
    else:
        print(" 11.  Numarul", x, "nu este pefect. Suma divizorilor este:", s)


_11(30)

# 12.------------------------------------------------------------------------------



def _12(a, b):
    r = []
    for i in range(a, b + 1):
        for j in range(i, b + 1):
            if i == reverse(j):
                r.append((i, j))
    print(" 12. ", r)
_12(10, 40)

# 13.----------------------------------------------------------------------------
def sum_digits(x):
    s = 0
    for digit in str(x):
        s = s + int(digit)
    return s


def _13(n):
    r = []
    for i in range(n):
        if(is_prime(sum_digits(i))):
            r.append(i)
    print(" 13. ", r)

_13(25)

# 14.-------------------------------------------------------

def _14(n):
    if(n < 1 and n > 1000):
        print("Erorr: Ati introdus o valoare care nu se incadreaza in interval")
        return -1

    d = []
    s = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            d.append(i)
            s = s + i
    print(" 14. ", d)
    print("      Suma divizorilor:", s)


_14(20)


# 15.-------------------------------------------------------------------

def _15(n, m):
    r = []
    i = 1
    while(len(r) < n):
        if(sum_digits(i) <= m):
            r.append(i)
        i = i + 1
    print(" 15. ", r)

_15(10, 4)


# 16.----------------------------------------------------------------

def _16(n):
    r = []
    for i in range(1, n):
        if(i % sum_digits(i) == 0):
            r.append(i)
    print(" 16. ", r)

_16(25)

# 17.------------------------------------------------------------

# Returneaza
def closest_num_to_divide(n):
    i = 2
    while(True):
        if(n % i == 0):
            return i
        i = i + 1


def _17(n):
    r = []
    print(" 17. ")
    while(True):
        if(n == 1):
            break

        print("     ", n, " | ", closest_num_to_divide(n))
        n = n / closest_num_to_divide(n)
    print("     ", 1, " |")

_17(3268)

# 18.--------------------------------------------------------------

def is_odd(n):
    if(n % 2 != 0):
        return True
    else:
        return False

def _18(n):
    r = []
    for i in range(n + 1):
        if(is_odd(sum_digits(i))):
            r.append(i)
    print(" 18. ", r)

_18(15)


# 19.-------------------------------------------------

def _19():
    r = []
    for i in range(10, 100):
        cat = i // 15
        rest = i % 15
        if cat ** 2 == rest:
            r.append(i)
    print(" 19. ", r)

_19()

# 20.---------------------------------------------------------

def _20(p, q):
    r = []
    k = 0
    for i in range(p, q + 1):
        if(is_prime(i)):
            r.append(i)
            k = k + 1
    print(" 20. ", r, "\n      Au fost gasite", k, "numere prime")

_20(10, 25)
