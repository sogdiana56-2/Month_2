from datetime import datetime as dt


def checktime(func):
    print(func.__name__)
    def wrapper(*args, **kwargs):


        time_now = dt.now()
        print(time_now.year)  # текущий год
        print(time_now.month)  # текущий месяц
        print(time_now.day)  # текущее число
        print(time_now.hour)  # текущий час
        print(time_now.minute)  # текущая минута
        print(time_now.second)  # текущая секунда

        print(f"До вызова ф-ии {func.__name__}")
        result = func(*args, **kwargs)
        print(f"После вызова ф-ии {func.__name__}")
        return result

    return wrapper


@checktime
def hello_world():
    print("hello world")


hello_world()

