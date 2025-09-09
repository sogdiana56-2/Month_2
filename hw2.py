class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}. "
              f"Моя профессия: {self.occupation}. У меня {education_status}.")

class Classmate:
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, я одноклассница Барби, мы учимся в {self.group_name} я родилась {self.birth_date}, работаю {self.occupation}")

classmate1 = Classmate("Скиппер", "2003", "Студентка", False, "11a")
classmate2 = Classmate("Тереза", "1998", "Фотограф", True, "11a")


class Friend:
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, я подруга Барби, я родилась {self.birth_date}, работаю {self.occupation}, мое хобби {self.hobby}")

friend1 = Friend("Кен","1995","Спортсмен",True, "чинить машины")
friend2 = Friend("Хлоя", "1994", "Модель", True, "танцевать")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()