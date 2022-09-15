from utils import load_students
from utils import load_professions
from utils import get_student_by_pk
from utils import get_profession_by_title


students = load_students()
professions = load_professions()


def check_fitness(student, profession):
    """
    получив студента и профессию, возвращет словарь c соответствием студента профессии
    :param student:
    :param profession:
    :return: check_fitness, student_has, student_lacks
    """
    # создаю сет с навыками выбранного студента и с профессиональными навыками
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    # определяю, какие нужные для професии навыки у студента есть.
    student_has = student_skills.intersection(profession_skills)
    # определяю, каких навыков у студента нет. Если у студента больше навыков, чем необходимо - пишу "-"
    if len(profession_skills) > len(student_has):
        student_lacks = profession_skills.difference(student_skills)
    else:
        student_lacks = "-"
    # считаю процент подходящести навыков и записываю в переменную fit_persent
    fit_persent = (len(student_has)*100//len(profession_skills))
    # записываю необходимые переменные в словарь
    check_fitness = {"has": [student_has], "lacks": [student_lacks], "fit_percent": fit_persent}

    return check_fitness, student_has, student_lacks


if __name__ == "__main__":

    pk = input("Введите номер студента: ")
    # программа проверяет, введено ли число. Если нет - выходит из программы.
    if pk.isdigit():
        student = get_student_by_pk(pk, students)
    else:
        print("Введите число")
        quit()

    # программа засчитает ввод, даже если пользователь введёт название с маленькой буквы
    title = input(f"Выберите специальность для оценки студента {student['full_name']}: ").title()
    profession = get_profession_by_title(title, professions)
    check_fitness, student_has, student_lacks = check_fitness(student, profession)

    # Программа выводит процент пригодности
    print(f"Пригодность {check_fitness['fit_percent']}%")
    student_has_str = ", ".join(student_has)

    # Программа выводит знания студента, и, если их нет - сообщает об этом
    if bool(student_has_str):
        print(f"{student['full_name']} знает {student_has_str}")
    else:
        print(f"{student['full_name']}  не имеет необходимых знаний")

    # Программа выводит то, что студент не знает
    student_lacks_str = ", ".join(student_lacks)
    print(f"{student['full_name']} не знает {student_lacks_str}")
