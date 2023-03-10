from collections import defaultdict

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if self.balance < value:
            print('Не хватает средств на балансе. Пополните счет')
        else:
            self.balance -= value
            return True

class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, product, count=1):
        self.goods[product] = self.goods.get(product, 0) + count
        self.__total += product.price * count

    def remove(self, product, count=1):
        if self.goods[product] > count:
            self.goods[product] -= count
            self.__total -= product.price * count
        else:
            self.__total -= product.price * self.goods[product]
            del self.goods[product]

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for key, value in sorted(self.goods.items(), key=lambda x: x[0].name):
            print(f'{key.name} {key.price} {value} {key.price * value}')
        print(f'---Total: {self.total}---')