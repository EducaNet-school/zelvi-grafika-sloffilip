text = input("Zadej větu").lower()
text2 = ""

for char in text:
    if char.isalnum():
        text2+=char
dict = {}
for char in text2:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

od = (sorted(dict.items()))

print(od)




