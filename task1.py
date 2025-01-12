import doctest

class Smartphone:
    def __init__(self, brand: str, model: str, storage_gb: int, battery_capacity_mAh: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param storage_gb: Объем встроенной памяти в гигабайтах
        :param battery_capacity_mAh: Емкость батареи в миллиампер-часах

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы (например, отрицательные значения)

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 128, 3200)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд смартфона должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть строкой")
        if not isinstance(storage_gb, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if not isinstance(battery_capacity_mAh, int):
            raise TypeError("Емкость батареи должна быть целым числом")
        if storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        if battery_capacity_mAh <= 0:
            raise ValueError("Емкость батареи должна быть положительным числом")

        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_capacity_mAh = battery_capacity_mAh
        self.current_battery_mAh = battery_capacity_mAh

    def make_call(self, duration_minutes: int) -> None:
        """
        Совершает звонок указанной длительности.

        :param duration_minutes: Длительность звонка в минутах

        :raise TypeError: Если duration_minutes не целое число
        :raise ValueError: Если duration_minutes отрицательно

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S21", 256, 4000)
        >>> phone.make_call(10)
        """
        if not isinstance(duration_minutes, int):
            raise TypeError("Длительность звонка должна быть целым числом")
        if duration_minutes < 0:
            raise ValueError("Длительность звонка не может быть отрицательной")
        # Логика уменьшения заряда батареи пропущена
        ...

    def install_app(self, app_name: str) -> None:
        """
        Устанавливает приложение на смартфон.

        :param app_name: Название устанавливаемого приложения

        :raise TypeError: Если app_name не строка
        :raise ValueError: Если app_name пустая строка

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 6", 128, 3700)
        >>> phone.install_app("WhatsApp")
        """
        if not isinstance(app_name, str):
            raise TypeError("Название приложения должно быть строкой")
        if not app_name.strip():
            raise ValueError("Название приложения не может быть пустой строкой")
        # Логика установки приложения пропущена
        ...


class Bicycle:
    def __init__(self, brand: str, model: str, gear_count: int, type_bike: str):
        """
        Создание и подготовка к работе объекта "Велосипед"

        :param brand: Бренд велосипеда
        :param model: Модель велосипеда
        :param gear_count: Количество передач
        :param type_bike: Тип велосипеда (например, "горный", "шоссейный")

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы


                Примеры:
                >>> bike = Bicycle("Trek", "Marlin 7", 21, "горный")
                """
        if not isinstance(brand, str):
            raise TypeError("Бренд велосипеда должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель велосипеда должна быть строкой")
        if not isinstance(gear_count, int):
            raise TypeError("Количество передач должно быть целым числом")
        if not isinstance(type_bike, str):
            raise TypeError("Тип велосипеда должен быть строкой")
        if gear_count <= 0:
            raise ValueError("Количество передач должно быть положительным числом")
        if not type_bike.strip():
            raise ValueError("Тип велосипеда не может быть пустой строкой")

        self.brand = brand
        self.model = model
        self.gear_count = gear_count
        self.type_bike = type_bike

    def change_gears(self, gear_number: int) -> None:
        """
        Переключает передачу на указанную.

        :param gear_number: Номер передачи

        :raise TypeError: Если gear_number не целое число
        :raise ValueError: Если gear_number вне допустимого диапазона

        Примеры:
        >>> bike = Bicycle("Giant", "Escape 3", 18, "городской")
        >>> bike.change_gears(5)
        """
        if not isinstance(gear_number, int):
            raise TypeError("Номер передачи должен быть целым числом")
        if not (1 <= gear_number <= self.gear_count):
            raise ValueError(f"Номер передачи должен быть между 1 и {self.gear_count}")
        # Логика переключения передач пропущена
        ...

    def ring_bell(self) -> None:
        """
        Звонит в звонок велосипеда.

        Примеры:
        >>> bike = Bicycle("Cannondale", "Trail 7", 24, "горный")
        >>> bike.ring_bell()
        """
        # Логика звонка пропущена
        ...

    class CoffeeMachine:
        def __init__(self, brand: str, model: str, water_capacity_liters: float, bean_capacity_grams: float):
            """
            Создание и подготовка к работе объекта "Кофемашина"

            :param brand: Бренд кофемашины
            :param model: Модель кофемашины
            :param water_capacity_liters: Вместимость резервуара для воды в литрах
            :param bean_capacity_grams: Вместимость контейнера для кофе в граммах

            :raise TypeError: Если типы аргументов не соответствуют ожидаемым
            :raise ValueError: Если значения аргументов не допустимы

            Примеры:
            >>> machine = CoffeeMachine("DeLonghi", "Magnifica", 2.0, 250.0)
            """
            if not isinstance(brand, str):
                raise TypeError("Бренд кофемашины должен быть строкой")
            if not isinstance(model, str):
                raise TypeError("Модель кофемашины должна быть строкой")
            if not isinstance(water_capacity_liters, (int, float)):
                raise TypeError("Вместимость воды должна быть числом")
            if not isinstance(bean_capacity_grams, (int, float)):
                raise TypeError("Вместимость кофе должна быть числом")
            if water_capacity_liters <= 0:
                raise ValueError("Вместимость воды должна быть положительным числом")
            if bean_capacity_grams <= 0:
                raise ValueError("Вместимость кофе должна быть положительным числом")

            self.brand = brand
            self.model = model
            self.water_capacity_liters = water_capacity_liters
            self.bean_capacity_grams = bean_capacity_grams
            self.current_water = water_capacity_liters
            self.current_beans = bean_capacity_grams

        def brew_coffee(self, water_liters: float, beans_grams: float) -> None:
            """
            Заваривает кофе с указанным количеством воды и кофе.

            :param water_liters: Количество воды в литрах
            :param beans_grams: Количество кофе в граммах

            :raise TypeError: Если параметры не числа
            :raise ValueError: Если параметры отрицательны или превышают текущие запасы


                    Примеры:
                    >>> machine = CoffeeMachine("Nespresso", "Vertuo", 1.5, 200.0)
                    >>> machine.brew_coffee(0.2, 10.0)
                    """
            if not isinstance(water_liters, (int, float)):
                raise TypeError("Количество воды должно быть числом")
            if not isinstance(beans_grams, (int, float)):
                raise TypeError("Количество кофе должно быть числом")
            if water_liters <= 0:
                raise ValueError("Количество воды должно быть положительным числом")
            if beans_grams <= 0:
                raise ValueError("Количество кофе должно быть положительным числом")
            if water_liters > self.current_water:
                raise ValueError("Недостаточно воды для заваривания кофе")
            if beans_grams > self.current_beans:
                raise ValueError("Недостаточно кофе для заваривания")
            self.current_water -= water_liters
            self.current_beans -= beans_grams
            # Логика заваривания кофе пропущена
            ...

        def refill_water(self, liters: float) -> None:
            """
            Заполняет резервуар для воды на указанное количество литров.

            :param liters: Количество литров для добавления

            :raise TypeError: Если liters не число
            :raise ValueError: Если liters отрицательно или превышает вместимость резервуара

            Примеры:
            >>> machine = CoffeeMachine("Breville", "Barista", 2.0, 300.0)
            >>> machine.refill_water(1.0)
            """
            if not isinstance(liters, (int, float)):
                raise TypeError("Количество литров должно быть числом")
            if liters <= 0:
                raise ValueError("Количество литров должно быть положительным числом")
            if self.current_water + liters > self.water_capacity_liters:
                raise ValueError("Переполнение резервуара для воды")
            self.current_water += liters
            ...

        def add_beans(self, grams: float) -> None:
            """
            Добавляет кофе в контейнер.

            :param grams: Количество граммов для добавления

            :raise TypeError: Если grams не число
            :raise ValueError: Если grams отрицательно или превышает вместимость контейнера

            Примеры:
            >>> machine = CoffeeMachine("Krups", "Espresseria", 1.8, 250.0)
            >>> machine.add_beans(50.0)
            """
            if not isinstance(grams, (int, float)):
                raise TypeError("Количество граммов должно быть числом")
            if grams <= 0:
                raise ValueError("Количество граммов должно быть положительным числом")
            if self.current_beans + grams > self.bean_capacity_grams:
                raise ValueError("Переполнение контейнера для кофе")
            self.current_beans += grams
            ...

        if __name__ == "__main__":
            doctest.testmod()