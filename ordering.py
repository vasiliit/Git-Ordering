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
            print('Не зватает средств на балансе. Пополните счет')
        else:
            self.balance -= value
            return True

class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0