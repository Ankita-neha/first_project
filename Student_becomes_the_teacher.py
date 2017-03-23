lloyd = {                                   #Dictionaries that contains the students data
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


#These are the functions for the purpose of calculations

def average(numbers):
    total = float(sum(numbers)) / len(numbers)
    return total


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return .1 * homework + .3 * quizzes + .6 * tests


def get_letter_grade(score):                #Grades are assigned to particular set of marks
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    get_average(lloyd)


def get_class_average(students):            #average of the whole class
    results = []
    for student in students:
        total = get_average(student)
        results.append(total)
    return average(results)


students = [lloyd, alice, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))


