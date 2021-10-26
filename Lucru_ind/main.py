

d = {
    "one": "unu",
    "two": "doi",
    "three": "trei",
    "four": "patru",
    "five": "cinci"
    }

f1 = open("./text.txt", "r")

text = ""

for line in f1:
    text += line

l = text.split()

for word in enumerate(l):
    if word == "one":
        word = "unu"
    elif word == "two":
        word = "doi"
    elif word == "three":
        word = "trei"
    elif word == "four":
        word = "patru"
    elif word == "five":
        word = "cinci"

print(l)