class Phone:
    """
    Базовый класс для всех телефонов.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация атрибутов телефона.
        :param brand: Марка телефона.
        :param model: Модель телефона.
        :param year: Год выпуска телефона.
        """
        self.__brand = brand  # Инкапсуляция, чтобы защитить марку от изменения извне
        self.__model = model  # Инкапсуляция, чтобы защитить модель от изменения извне
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление телефона."""
        return f"{self.year} {self.__brand} {self.__model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление телефона."""
        return f"Phone(brand='{self.__brand}', model='{self.__model}', year={self.year})"

    def make_call(self, number: str) -> str:
        """
        Совершает звонок на указанный номер.
        :param number: Номер телефона для звонка.
        :return: Сообщение о звонке.
        """
        return f"Calling {number} from {self.__brand} {self.__model}."


class Smartphone(Phone):
    """
    Класс для смартфонов, наследует от Phone.
    """

    def __init__(self, brand: str, model: str, year: int, os: str) -> None:
        """
        Инициализация атрибутов смартфона.
        :param brand: Марка смартфона.
        :param model: Модель смартфона.
        :param year: Год выпуска смартфона.
        :param os: Операционная система смартфона.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.os = os

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона."""
        return f"{super().__str__()} running {self.os}"

    def install_app(self, app_name: str) -> str:
        """
        Устанавливает приложение на смартфон.
        :param app_name: Название приложения.
        :return: Сообщение об установке приложения.
        """
        return f"Installing {app_name} on {self.__brand} {self.__model}."


class FeaturePhone(Phone):
    """
    Класс для кнопочных телефонов, наследует от Phone.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация атрибутов кнопочного телефона.
        :param brand: Марка кнопочного телефона.
        :param model: Модель кнопочного телефона.
        :param year: Год выпуска кнопочного телефона.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса

    def __str__(self) -> str:
        """Возвращает строковое представление кнопочного телефона."""
        return f"{super().__str__()} (Feature Phone)"

    def send_sms(self, number: str, message: str) -> str:
        """
        Отправляет SMS на указанный номер.
        :param number: Номер телефона для отправки SMS.
        :param message: Сообщение для отправки.
        :return: Сообщение об отправке SMS.
        """
        return f"Sending SMS to {number}: '{message}' from {self.__brand} {self.__model}."


# Примеры использования классов
if __name__ == "__main__":
    my_smartphone = Smartphone("Apple", "iPhone 13", 2021, "iOS")
    print(my_smartphone)  # Выводит информацию о смартфоне
    print(my_smartphone.make_call("123-456-7890"))  # Звонок с смартфона
    print(my_smartphone.install_app("WhatsApp"))  # Установка приложения

    my_feature_phone = FeaturePhone("Nokia", "105", 2019)
    print(my_feature_phone)  # Выводит информацию о кнопочном телефоне
    print(my_feature_phone.make_call("098-765-4321"))  # Звонок с кнопочного телефона
    print(my_feature_phone.send_sms("098-765-4321", "Hello!"))  # Отправка SMS
