from utils import load_questions
import random


class Question:

    def __init__(self, name, q, d, a):
        self.name = name
        self.q = q
        self.d = d
        self.a = a
        self.is_answer = False
        self.user_answer = None
        self.point = self.get_points()

    def get_points(self) -> int:
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        point = int(self.d) * 10
        return point

    def is_correct(self, user_answer) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом
        """
        if user_answer == self.a:
            return True

    def build_question(self) -> None:
        """
        Возвращает вопрос в понятном пользователю виде, с указанием сложности
        """
        if self.is_answer is not True:
            question_for_user = self.q
            difficulty = f"{self.d}/5"
            print(f"\nВопрос: {question_for_user}\nСложность: {difficulty}")

    def build_positive_feedback(self) -> None:
        """
        Выводит количество баллов, полученное пользователем за верный ответ
        """
        print(f"Ответ верный, получено {self.point} баллов")

    def build_negative_feedback(self) -> None:
        """
        Выводит количество баллов, полученное пользователем за неверный ответ
        """
        print(f"Ответ неверный, баллы не начисляются. Верный ответ {self.a}")


def pack_questions_in_list() -> list:
    """
    Упаковывает в список экземпляры класса Question
    """
    questions = load_questions()
    questions_list = []
    for i in range(len(questions)):
        question = Question(f"question {i+1}", questions[i]["q"], questions[i]["d"], questions[i]["a"])
        questions_list.append(question)
    return questions_list


def statistics(questions_list, scores) -> None:
    """
    Выводит статистику игры
    """
    print("\nВот и всё!")
    correct_count = 0
    for question in questions_list:
        if question.is_answer is True:
            correct_count += 1
    print(f"\nОтвечено вопросов {correct_count} из {len(questions_list)}")
    print(f"Набрано баллов: {scores}")


def main():
    """
    Основная логика игры
    """
    scores = 0
    questions_list = pack_questions_in_list()
    random.shuffle(questions_list)
    print(f"\nИгра началась!")
    for question in questions_list:
        question.build_question()
        user_answer = input(f"\nВведите ваш ответ: ")

        if question.is_correct(user_answer):

            question.is_answer = True
            question.user_answer = user_answer
            scores += int(question.point)

            question.build_positive_feedback()

        else:
            question.user_answer = user_answer

            question.build_negative_feedback()

    statistics(questions_list, scores)


if __name__ == "__main__":
    main()
