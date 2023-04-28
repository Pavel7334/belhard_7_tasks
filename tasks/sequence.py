"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:

    def __init__(self, n: int) -> None:
        self.n = n
        self.sequence = []
        self.generate()

    def generate(self, m=None) -> None:
        n = m or self.n
        self.sequence = [random.randint(-n, n) for _ in range(n)]

    def print_seq(self) -> None:
        print(f"Вот такая последовательность {self.sequence}")


sequ = RandSequence(10)
sequ.print_seq()
sequ.generate()
sequ.print_seq()
