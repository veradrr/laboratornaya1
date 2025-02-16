
class City:
    """
    Базовый класс "Город"
    """
    def __init__(self, name: str, population: int):
        """
        Создание и подготовка к работе объекта "Город"

        :param name: название города
        :param population: население города
        Примеры:
            >>> moscow = City('Moscow', 15000000)  # инициализация экземпляра класса
        """
        self._name = name
        self._population = population

    @property
    def name(self) -> str:
        """Возвращает название города"""
        return self._name

    @property
    def population(self) -> int:
        """Возвращает население города"""
        return self._population

    @population.setter
    def population(self, value: int):
        """
        Устанавливает новое значение населения.
        Проверяет, что население не может быть отрицательным.
        """
        if value <= 0:
            raise ValueError("Население не может быть отрицательным!")
        self._population = value

    def __str__(self):
        return f"Город {self._name}, население {self._population}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, population={self._population!r})"


class NewYork(City):
    """
    Дочерний класс "Нью-Йорк", унаследованный от "Город"
    """

    def __init__(self, population: int, boroughs: int):
        """
        Создание объекта "Нью-Йорк"

        :param population: население Нью-Йорка
        :param boroughs: количество районов в городе
        """
        super().__init__("New York", population)
        self._boroughs = boroughs

    @property
    def boroughs(self) -> int:
        """Возвращает количество районов в Нью-Йорке"""
        return self._boroughs

    def __str__(self):
        return f"Город {self._name}, население {self._population}, районов: {self._boroughs}"

    def __repr__(self):
        return f"{self.__class__.__name__}(population={self._population!r}, boroughs={self._boroughs!r})"


if __name__ == "__main__":
    nyc = NewYork(8500000, 5)  # Создаем объект
    print(nyc)  # Город New York, население 8500000, районов: 5
    print(nyc.population)  # 8500000
    nyc.population = 9000000  # Изменяем население
    print(nyc.population)  # 9000000
