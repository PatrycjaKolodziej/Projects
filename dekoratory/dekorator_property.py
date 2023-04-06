class Employee:
    def __init__(self, f_name: str, l_name: str, age: int) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.__age = age

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, new_age):
        self.__age = new_age


p1 = Employee("Jan", "Kowalski", 30)
p1.f_name = "Adam"
print(p1.f_name)
p1.age = 42
print(p1.age)



# Napisz klasę o nazwie Product, która zawiera pole:
#     - nazwa (str)
#     - kategoria (str)
#     - sn (str)
#     - price (float)
#
# Zmienne sn oraz price są prywatne,
#     a dostęp do nich jest możliwy dzięki getter/setter
#
# Dodatkowo nie można ustawić price na wartość mniejszą niż 0.01
#     (próba ustawienia wartości mniejszej niż 0.01 powoduje ustawienie 0.01)


class Product:
    def __init__(self, name, category, sn, price):
        self.name = name
        self.category = category
        self.__sn = sn

        if price < 0.01:
            self.__price = 0.01
        else:
            self.__price = price
    @property
    def sn(self):
        return self.__sn

    @property
    def price(self):
        return self.__price

    @sn.setter
    def sn(self, new_sn):
        self.__sn = new_sn

    @price.setter
    def price(self, new_price):
        if new_price < 0.01:
            self.__price = 0.01
        else:
            self.__price = new.price

p1 = Product("Intel i7", "CPU", "000-000-0001", 4999.99)