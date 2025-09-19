class User:
    # переменные класса
    total_users = 0
    def __init__(self, name, emal):
        self.name = name
        self.emal = emal
        User.total_users += 1

    @classmethod
    def get_total_user (cls):
        return cls.total_users

    @staticmethod
    def validate_email(email):
        return "@" in email


print(User.total_users)


user_1 = User("igor", "igor@gmail.com")
user_2 = User("Albert", "albrt@gmail.com")

user_1.total_users = 4

print(User.total_users)
print(User.total_users)