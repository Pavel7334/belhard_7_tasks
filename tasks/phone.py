"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:

    def __init__(self, brand: str, model: str, issue_year: int) -> None:
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name) -> None:
        print(f'Звонит {name}')

    def get_info(self) -> tuple:
        return self.brand, self.model, self.issue_year

    def __str__(self) -> str:
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"


phone = Phone('Ford', 'focus', 20)
print(phone.get_info())
phone.receive_call('Павел')
