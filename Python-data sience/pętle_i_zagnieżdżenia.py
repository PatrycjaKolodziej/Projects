accounts = [
    ("A001", "100600", 250.50),
    ("B001", "200800", 1999.97),
    ("A002", "600100", 62780.00)
]

print(accounts)
print(accounts[-1])
print(accounts[-1][2])

# Dla przykładu powyżej:
#             0         1       2
#     0   [0][0]   [0][1]   [0][2]
#     1
#     2
print(accounts)
print(accounts[0][2], accounts[1][2])

# Pętle for
# 1. Łańcuch znakowy
for c in "KOTEK":
    print("Litera:", c)

# 2. Łańcuch znakowy -> lista
for word in "Ala ma kota".split(" "):
    print("Słowo:", word)

# 3. Lista/Krotka
for element in accounts:
    print("Klient:", element)

# 4. Sekwencja liczb (range)
# range(start, end, step)  |  <start, end-1>
# Domyślnie krok = 1
# range(10) - <0,9>
# range(1,12) - <1,11>
# range(2,10,2) - <2,9> z krokiem 2

for i in range(1,12):
    print("Liczba:", i)

for i in range(2,10,2):   # co 2
    print("Liczba:", i)

# 4. Ciąg malejący
for i in range(10, 1, -1):   # maleje od 10 do 1 co 1 krok
    print(i)




data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]

data_in_dict = {}

print(data[0][0], data[0][1])

for i in range(len(data)):
    if data[i][0] not in data_in_dict.keys():
        data_in_dict[ data[i][0] ] = data [i][1] / 50

print(data_in_dict)


txt = "alamakotaakotmapierdolca"

def char_counter(text: str) -> dict:
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = text.count(c)

    return result

print(char_counter(txt))


# While

n = 0
while n < 10:
    print(n ** 2)
    n += 1


txt = "ala-ma-kota"
n = 0

while n < len(txt):
    print(txt[n])
    n += 1








