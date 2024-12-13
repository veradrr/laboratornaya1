from typing import Union
import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Coffee:
    def __init__(self, strength: int, milk: int):
        """
        Создание и подготовка к работе объекта "Кофе"

        :param strength: крепкость
        :param milk: количество молока

        Примеры:
        >>> drink = Coffee(10, 0)  # инициализация экземпляра класса
        """
        if not isinstance(strength, int):
            raise TypeError("Крепкость кофе должна быть числом")
        if strength not in range(1,11):
            raise ValueError("Крепкость должна быть в диапазоне от 1-10")

        self.strength = 5 #значение по умолчанию

        if not isinstance(milk, int):
            raise TypeError("Количество молока должно быть числом")
        if milk not in range(0,4):
            raise ValueError("Количество молока должно быть в диапазоне от 0-3")

        self.milk = 2
    def bad_drink(self) -> bool:
        """
        Функция которая проверяет будет ли кофе горьким

        :return: Является ли кофе горьким (если сумма крепкости и молока больше 8, то горький)

        Примеры:
        >>> drink = Coffee(10, 0)
        >>> drink.bad_drink()
        """
    def watery(self, water: int) -> None:
        """
        Разбавить кофе водой.
        :param water: Объем добавляемой жидкости

        Примеры:
        >>> drink = Coffee(10, 0)
        >>> drink.watery(100)
        """
        if not isinstance(water, int):
            raise TypeError("Добавляемая жидкость должна быть числом")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

class Studio:
    def __init__(self, friends: int, days: int):
        """
        Создание и подготовка к работе объекта "Студия"

        :param friends: Количество приглашенных друзей в квартиру-стуию
        :param days: Сколько дней они планируют оставаться

        Примеры:
        >>> slightly_annoying = Studio(2, 5)  # инициализация экземпляра класса
        """
        if not isinstance(friends, int):
            raise TypeError("Друзья только целые")
        self.friends = friends
        if not isinstance(friends, int):
            raise TypeError("Количество дней можеть быть только целым числом")
        self.days = days

    def when_to_kick_out(self) -> bool:
        """
        Функция которая проверяет когда друзья перестают нравиться

        :return: Стоит ли попросить их съехать

        Примеры:
        >>> annoying = Studio(4, 10)
        >>> annoying.when_to_kick_out()
        """
        ...

    def how_many_to_kick_out(self, lost_friends: float) -> None:
        """
        Функция которая проверяет сколько друзей можно выгнать

        :param lost_friends: Сколько друзей мы попросили съехать
        :raise ValueError: Если количество съехавших друзей больше чем чем приехавших(останемся одни), возвращается ошибка

        :return: Остаток друзей

        Примеры:
        >>> annoying = Studio(4, 10)
        >>> annoying.how_many_to_kick_out(8)
        """
        ...

class BankAccount:
    def __init__(self, account_number: int, owner: str, money: float):
        """
        Создание и подготовка к работе объекта "Счет в банке"

        :param account_number: Номер счета
        :param owner: Фамилия владельца
        :param money: Количество денег на счету


        Примеры:
        >>> pokupka = BankAccount(775622, "Green", 200)  # инициализация экземпляра класса
        """
        if not isinstance(account_number, int):
            raise TypeError("Номер счета может быть только целым числом")
        if account_number <= 99999:
            raise ValueError("Номер счета моет быть только положительным 6-ти значным числом")
        self.account_number = account_number

        if not isinstance(owner, str):
            raise TypeError("Фамилия должна быть написана буквами")
        self.owner = owner

        if not isinstance(money, (int, float)):
            raise TypeError("Остаток по счету можеть быть только типа int или float")
        self.money = money

    def do_they_owe_us(self) -> bool:
        """
        Функция которая проверяет должен ли банку владелец аккаута(если money отриц, то должен)

        Примеры:
        >>> info = BankAccount(775622, "Musk", -2000)
        >>> info.do_they_owe_us()
        """
        ...

    def popolnenye_scheta(self, add: float) -> None:
        """
        Пополнение счета в банке
        :param add: Сумма на которую человек пополняет счет

        Примеры:
        >>> zarplata = BankAccount(766622, "Ivanov", 350000)
        >>> zarplata.popolnenye_scheta(40000)
        """
        if not isinstance(add, (int, float)):
            raise TypeError("Мы можем добавить только число")
        if add < 0:
            raise ValueError("Пополнение только на положительную сумму")
        ...
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
