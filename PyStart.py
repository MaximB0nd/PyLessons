# Есть список строк лога в формате: "<уровень>: <сообщение>".
# Нужно:
#
# Разделить строки на уровень логирования и сообщение, используя распаковку.
# Подсчитать количество записей для каждого уровня (INFO, WARN, ERROR), используя словарь.
# Сформировать список только сообщений (без уровня), которые относятся к уровню ERROR.

log_lines = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "WARN: Disk space is low",
    "INFO: Request processed",
    "ERROR: File not found",
    "WARN: Unexpected input",
    "ERROR: Permission denied"
]

def parse_logs(log_entries):

    counter = {}
    errors = []

    for line in log_entries:
        level, error = line.split(":", 1)
        error = error.strip()
        if counter.get(level):
            counter[level] += 1
        else:
            counter[level] = 1
        if level == "ERROR":
            errors.append(error)

    return counter, errors

def another_parse_log(log_entries):
    counter = {}
    splited = [entry.split(":", 1) for entry in log_entries]
    for level, _ in splited:
        counter[level] = counter.get(level, 0) + 1
    errors = [error.strip() for level, error in splited if level == "ERROR"]
    return counter, errors

if __name__ == "__main__":
    print(parse_logs(log_lines) == another_parse_log(log_lines))



