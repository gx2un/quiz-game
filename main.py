class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number):
        print("-" * 40)
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


def get_default_quizzes():
    """기본 퀴즈 목록을 반환한다."""
    return [
        Quiz(
            "Python 언어를 처음 만든 사람은?",
            ["리누스 토르발스", "제임스 고슬링", "귀도 반 로섬", "비야네 스트롭스트룹"],
            3,
        ),
        Quiz(
            "다음 중 int 자료형인 값은?",
            ["42", "3.14", '"42"', "[42]"],
            1,
        ),
        Quiz(
            "반복문을 즉시 빠져나갈 때 사용하는 키워드는?",
            ["continue", "pass", "return", "break"],
            4,
        ),
        Quiz(
            "Python에서 변경할 수 없는 자료형은?",
            ["list", "dict", "tuple", "set"],
            3,
        ),
        Quiz(
            "input() 함수가 반환하는 값의 자료형은?",
            ["int", "str", "float", "bool"],
            2,
        ),
    ]


def show_menu():
    print("=" * 40)
    print("        Python 기초 퀴즈")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

def main():
    quizzes = get_default_quizzes()
    while True:
        show_menu()
        choice = get_number("선택 : ", 1, 5)

        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            add_quiz(quizzes)
        elif choice == 3:
            list_quizzes(quizzes)
        elif choice == 4:
            print("점수 확인 (준비 중)")
        else:
            print("프로그램을 종료합니다.")
            break


def get_number(prompt, min_value, max_value):
    """min_value ~ max_value 사이의 정수를 입력받아 반환한다."""

    while True:
        text = input(prompt).strip()
        if text == "":
            print("값을 입력해주세요.")
            continue


        try:
            number = int(text)
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if number < min_value or number > max_value:
            print(f"{min_value}~{max_value} 사이의 숫자를 입력해주세요.")
            continue

        return number


def get_text(prompt):
    """빈 값이 아닌 문자열을 입력받아 반환한다."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("내용을 입력해주세요.")
            continue
        return text


def play_quiz(quizzes):
    """퀴즈를 순서대로 출제하고 결과를 보여준다."""
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    print(f"\n 퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    correct_count = 0

    for i, quiz in enumerate(quizzes, 1):
        quiz.display(i)
        answer = get_number("정답 입력: ", 1, 4)

        if quiz.is_correct(answer):
            print("정답입니다!")
            correct_count += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번 입니다.")

    score = round(correct_count / len(quizzes) * 100)
    print("=" * 40)
    print(f"결과: {len(quizzes)}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)

def add_quiz(quizzes):
    """새 퀴즈를 입력받아 목록에 추가한다."""
    print("\n새로운 퀴즈를 추가합니다.")

    question = get_text("문제를 입력하세요: ")

    choices = []
    for i in range(1,5):
        choice = get_text(f"선택지 {i}: ")
        choices.append(choice)

    answer = get_number("정답 번호 (1-4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)

    print("퀴즈가 추가되었습니다!")

def list_quizzes(quizzes):
    """등록된 퀴즈의 문제 목록을 보여준다."""
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return
    print(f"등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("-" * 40)
    for i, quiz in enumerate(quizzes, 1):
        print(f"[{i}] {quiz.question}")
    print("-" * 40)


if __name__ == "__main__":
    main()


