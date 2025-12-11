from argparse import ArgumentTypeError
from functools import wraps

def my_decorator(func):
    def wrapper():
        print("Starter function")
        func()
        print("End function")
   
@my_decorator
def say_hello():
    print("Hello World")
    
def smart_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        
@smart_decorator
def say_hello_to(name):
    print("Hello to", name)
    
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            resuts = []
            for i in range(times):
                result = func(*args, **kwargs)
                resuts.append(result)
            return resuts
        return wrapper
    return decorator

@repeat_decorator(times=3)
def say_hello_to(name):
    print("Hello to", name)
    
def correct_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper
    
@correct_decorator
def original():
    """Оригинальная функция"""
    pass

def cache(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]
    return wrapper
    
@cache
def say_hello_to(name):
    print("Hello to", name)

# Задача написать
# validate_arguments — проверяет, что все числовые аргументы положительные
# log_to_file — записывает в файл информацию о вызове функции

def validate_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, (int, float)) and int(arg) < 0:
                raise ArgumentTypeError("Invalid argument")
        return func(*args, **kwargs)
    return wrapper

def log_to_file(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, "a") as log:
                log.write(func.__name__ + "\n" + func.__doc__)
            return func(*args, **kwargs)
        return wrapper
    return decorator
    
@log_to_file("Resources/rect.txt")
@validate_arguments
def calculate_rectangle_area(length, width):
    """Вычисляет площадь прямоугольника"""
    return length * width

@log_to_file("Resources/tria.txt")
@validate_arguments
def calculate_triangle_area(base, height):
    """Вычисляет площадь треугольника"""
    return 0.5 * base * height
                
if __name__ == "__main__":
    print(calculate_rectangle_area(length=100, width=100))
    print(calculate_triangle_area(100, 100))