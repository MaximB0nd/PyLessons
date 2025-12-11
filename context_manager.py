# Напишите функцию process_files(source_file, target_file), которая:
#
# Открывает два файла одновременно (один для чтения, другой для записи) с использованием одного оператора with
# Читает данные из source_file
# Записывает в target_file только строки, содержащие слово "error" (без учета регистра)
# Подсчитывает количество обработанных строк
# Использует кастомный контекстный менеджер для логирования времени выполнения

from contextlib import contextmanager

def process_files(source_file, target_file):
    count = 0
    with Timer() as timer:
        with open(source_file, "r") as source, open(target_file, "w") as target:
            for line in source:
                if "error" in line.lower():
                    target.write(line)
                    count += 1
                    
    return count

@contextmanager
def my_context_manager(source_file, target_file):
    count = 0

class Timer():
    start = None
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end = time.time()
        print(f"Время выполнения: {time.time() - self.start:.2f} сек")





if __name__ == "__main__":
    source_file = "Resources/text1.txt"
    target_file = "Resources/text2.txt"
    process_files(source_file, target_file)
