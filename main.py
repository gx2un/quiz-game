import json
from pathlib import Path

STATE_FILE = Path(__file__).parent / "state.json"



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

    def to_dict(self):
        """JSON 저장을 위해 dict로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """dict에서 Quiz 객체를 만든다."""
        return cls(data["question"], data["choices"], data["answer"])


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
    quizzes, best_score = load_state()

    while True:
        show_menu()
        choice = get_number("선택 : ", 1, 5)

        if choice == 1:
            score = play_quiz(quizzes)
            if score is not None:
                if best_score is None or score > best_score:
                    best_score = score
                    print("새로운 최고 점수입니다!")
                    save_state(quizzes, best_score)
        elif choice == 2:
            add_quiz(quizzes)
            save_state(quizzes, best_score)
        elif choice == 3:
            list_quizzes(quizzes)
        elif choice == 4:
            show_score(best_score)
        else:
            save_state(quizzes, best_score)
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
        return None

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
    return score

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

def show_score(best_score):
    """최고 점수를 보여준다."""
    if best_score is None:
        print("아직 퀴즈를 풀지 않았습니다.")
        return
    print(f"최고 점수: {best_score}점")

def save_state(quizzes, best_score):
    """퀴즈 목록과 최고 점수를 state.json에 저장한다."""
    data = {
        "quizzes": [quiz.to_dict() for quiz in quizzes],
        "best_score": best_score,
    }
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError:
        print("데이터를 저장하지 못했습니다.")

def load_state():
    """state.json에서 퀴즈 목록과 최고 점수를 불러온다."""
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
        best_score = data["best_score"]
        print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {best_score}점)")
        return quizzes, best_score

    except FileNotFoundError:
        print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
        return get_default_quizzes(), None

    except (json.JSONDecodeError, KeyError, TypeError):
        print("데이터 파일이 손상되어 기본 퀴즈로 복구합니다.")
        return get_default_quizzes(), None
if __name__ == "__main__":
    main()


