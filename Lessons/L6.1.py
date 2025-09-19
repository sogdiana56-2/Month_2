
def printer(func):
    def wrapper(*args, **kwargs):
        print(f"до вызова функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"после вызова функции {func.__name__}")
        return result

        return wrapper


@printer
def hello_world():
    print("Hello World")


@printer
def add_numbers(number1, namber2):
    return number1 + namber2

hello_world()
print(add_numbers(1,2))

def dfghj():
    print("dfghj dfgh")
