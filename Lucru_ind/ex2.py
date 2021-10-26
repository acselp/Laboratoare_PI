f = open("nums.txt", "r")
text = f.read()

nums = text.split()
s = 0

for num in nums:
    s += int(num)

print("Suma numerelor din fisier este: ", s)