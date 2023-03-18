# # Prosta funkcja
# def show_sum(a,b):
#     print("Suma:", a + b)
#
# def add(a, b):
#     return a + b
#
# x = add(1, 9)
# print(x)
# print(add(99,101))

#
# def is_even(x):
#     return a % 2 == 0
#
# y = 11
# if is_even(y):
#     print("Parzysta")

    #
    # def my_pow(base, power):
    #     return base ** power

answer = int(input("Liczba prawidłowych odpowiedzi"))
questions = int(input("Liczba pytań"))
percent = answer / questions * 100

if 90 <= percent <= 100:
  print("Ocena: ", "5.0")
elif 76 <= percent <= 89:
  print("Ocena: ", "4.5")
elif 70 <= percent <= 75:
  print("Ocena: ", "4.0")
elif 60 <= percent <= 69:
  print("Ocena: " , "3.5")
elif 50 <= percent <= 59:
  print("Ocena: ", "3.0")
else:
  print("Ocena: ", "2.0")