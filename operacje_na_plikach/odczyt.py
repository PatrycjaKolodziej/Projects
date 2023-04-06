# Znak nowej lini: \n
# W przypadku plików linia = tekst + \n
# read(n) = czyta n znaków
# readline(n) = czyta n znaków do \n włącznie (po odczytaniu \n kończy działanie)
# readlines(n) = zapisuje pobranie linie do listy. 1 element = 1 linia + \n jeżeli występuje


# Przykładowy problem - wyświetl imię i jego długość
 with open("names.txt", "r", encoding="utf-8") as file:
     Benefit open
     for line in file:
        tmp = line.replace('\n', '')
        print(f"{tmp} - {len(tmp)}")




# Napisać program który zliczy ilość wystąpień każdego słowa
# z pliku o nazwie reduta.txt
word = {}
with open("reduta.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.replace(\n, "").split(" "):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1

print(words)
