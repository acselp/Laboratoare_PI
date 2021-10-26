



# Deschidem fiierul
f = open("./text.txt", "r")


text = ""

# Copiem toate liniile din fisier in variabila text
for line in f:
    text += line

f.close() # Inchidem fisierul

digits = [["one", "unu"], ["two", "doi"], ["three", "trei"], ["four", "patru"], ["five", "cinci"]]

# Inlocuim cifrele din el=ngleza cu cifrele din romana
for digit in digits:
    text = text.replace(digit[0], digit[1])

f = open("dataRo.txt", "a")
f.write(text)
f.close()
