class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родилась {self.birth_date}. "
              f"Моя профессия: {self.occupation}. У меня {education_status}.")


person1 = Person("Блум", "10.12.1994", "Фея драконьего пламени", True)
person2 = Person("Стелла", "18.08.1994", "Фея Солнца и Луны", True)
person3 = Person("Флора", "01.03.1995", "Фея Природы", True)
for person in (person1, person2, person3):
    print(f"Имя: {person.name}")
    print(f"Дата рождения: {person.birth_date}")
    print(f"Профессия: {person.occupation}")
    print(f"Высшее образование: {person.higher_education}")
    person.introduce()

