# Напишите функцию process_text(text), которая:

# Принимает строку текста
# Используя list comprehension, создает список слов длиной более 3 символов (в нижнем регистре)
# Используя dict comprehension, создает словарь {слово: количество_гласных}
# Использует генератор для последовательности чисел Фибоначчи до n (n передается параметром)

def process_text(text):
    words = text.split(" ")
    words_more_3 = [word.lower() for word in words if len(word) > 3]
    dictionary = {word: len([char for char in word if char in 'aeiou']) for word in words}
    return words_more_3, dictionary

def simple_generator():
    i = 0
    while True:
        yield i
        i += 1

def my_range(start, stop=None, step=1):
    now = start
    while now < stop:
        yield now
        now += step

if __name__ == "__main__":
    print(process_text(text = "Python is an amazing programming language!"))
    generator = simple_generator()
    next(generator)
    next(generator)


    