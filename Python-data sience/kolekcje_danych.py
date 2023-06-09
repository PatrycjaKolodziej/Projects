# Łańcuch znakowy jako kolekcja danych
txt = "Ala ma kota."

# Warunek na podstawie zbioru
if "kot" in txt:
    print("Ala faktycznie posiada kota.")

# Metody dla str
print(len(txt))
print(txt.upper())
print(txt.lower())
print(txt.isalnum())

# Powielanie tekstu
print(txt * 2)

# Indeksowanie | 0..(len - 1)
print(txt[0])_      # Wyświetl 1 znak
print(txt[:4])      # <0, 4)   |   <0, 3>
print(txt[2:8])     # <2, 8)   |   <2, 7>
print(txt[3:1])     # <3, len) |   <3, len-1>
print(txt[2:8:2])   # <2, 7>  co drugi = <2,4,6>
print(txt[::3])     # <cały tekst> co trzeci
print(txt[::-1])    # Od końca

#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -3 -2 -1

def reverse_ind(text, index)
    if 0 <= index <= (len(text) - 1):
        return index - len(text)
    else:
        return -999

print(reverse_idx("HELLO"))

## Lista ##
# values = [3, 4.67, "LOL", True, 11, "XD"] # Nie robić tak!
animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
# Pusta lista: empty = [] lub empty = list()

# Metody/Fukcje listy
print(len(animals))
print(animals[0], animals[-1], animals[2:4])
print(sum(numbers), max(numbers), min(numbers))

# Dodawanie
animals.append("Szynszyla")
print(animals)

animals.extend(["Mysz", "Kanarek"])
print(animals)

animals.insert(1, "Krokodyl")
print(animals)

# Usuwanie
animals.remove("Szynszyla")
print(animals)

animals.pop()_# Jeżeli nie podany idx, usuwamy ostatni element
print(animals)

animals.pop(2)
print(animals)
deleted_value = animals.pop(0)
print(animals, deleted_value)
deleted_arg.append(deleted_value)
print(animals, deleted_args)

# Modyfikacja
animals[0] = "Mrówka"
print(animals)

