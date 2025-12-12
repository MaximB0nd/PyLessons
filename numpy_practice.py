import numpy as np
from numpy.ma.extras import average

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

arr3 = np.zeros((3, 4))
arr4 = np.ones((3, 4))

arr_range = np.arange(0, 10, 2)
linspace = np.linspace(0, 10, 10)

# print(arr1.shape)
# print(arr1.ndim)
# print(arr1.size)
# print(arr1.dtype)
# 
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 ** arr2)
# 
# print(arr1[0])
# print(arr2[0, 0])
# print(arr1[0:4])

# Напишите функцию analyze_student_grades(students_grades, weights=None), которая:
# 
# Принимает список списков с оценками студентов (каждый вложенный список — оценки одного студента)
# Возвращает словарь со статистикой:
# 
# Средний балл по каждому студенту
# Средний балл по каждому предмету (если передан weights, то с учетом весов)
# Максимальный балл по каждому предмету
# Количество студентов с средним баллом > 4.0

def analyze_student_grades(students_grades, weights=None):
    students_grades = np.array(students_grades)
    result = {}
    result["student_averages"] = np.mean(students_grades, axis=1)
    result["subject_averages"] = np.mean(students_grades, axis=0)
    if weights:
        weights = np.array(weights)
        result["weighted_subject_averages"] = np.average(students_grades,axis=1, weights=weights)
    result["subject_max"] = np.max(students_grades)
    result["subject_min"] = np.min(students_grades)
    result["top_students_count"] = np.sum(np.where(students_grades > 4))
    
    return result

# Напишите функцию array_stats(arr), которая принимает 2D массив оценок студентов и возвращает:
# 
# Среднюю оценку по всем студентам
# Медиану по каждому предмету
# Количество студентов, у которых все оценки выше 3
# Массив булевых значений, где True — если студент имеет хотя бы одну оценку 5

def array_stats(arr):
    arr = np.array(arr)
    result = {}
    
    if arr.shape[1] != 3:
        raise ValueError("array must have shape (, 3)")
    
    result["mean_all"] = np.mean(arr)
    result["subject_medians"] = np.median(arr, axis=0)
    result["all_above_3"] = np.where(arr > 3)

    
    return result

if __name__ == "__main__":
    grades = [
        [5, 4, 5],  # Студент 1
        [3, 4, 2],  # Студент 2
        [4, 5, 5],  # Студент 3
        [2, 3, 4]  # Студент 4
    ]

    weights = [1.5, 1.0, 2.0]
    # for result in analyze_student_grades(grades, weights).values():
    #     print(result)

    test_grades = np.array([
        [5, 4, 3],
        [2, 3, 2],
        [4, 5, 5],
        [3, 4, 4]
    ])
    
    for result in array_stats(test_grades).values():
        print(result)

