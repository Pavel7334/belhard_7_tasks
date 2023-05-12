"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:

    def __init__(self, surname: str, name: str, group: int, average_score: int) -> None:
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __str__(self) -> str:
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nНомер группы: {self.group}\nСредний бал: {self.average_score}"

    def __eq__(self, other) -> int:
        return self.average_score == other.average_score

    def __ne__(self, other) -> int:
        return self.average_score != other.average_score

    def __lt__(self, other) -> int:
        return self.average_score < other.average_score

    def __gt__(self, other) -> int:
        return self.average_score > other.average_score

    def __le__(self, other) -> int:
        return self.average_score <= other.average_score

    def __ge__(self, other) -> int:
        return self.average_score >= other.average_score


student_1 = Student('Вася', 'Васильев', 1, 3)
student_2 = Student('Петя', 'Петров', 2, 4)
student_3 = Student('Иван', 'Иванов', 3, 5)
student_4 = Student('Сергей', 'Сергеев', 4, 5)
student_5 = Student('Алексей', 'Алексеев', 2, 2)

lst = ([student_1, student_2, student_3, student_4, student_5])


def sort_by_average_score(self):
    return self.average_score


lst.sort(key=sort_by_average_score)
print(lst)
