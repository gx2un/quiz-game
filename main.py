
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
    while True:
        show_menu()
        choice = get_number("선택 : ", 1, 5)

        if choice == 1:
            print("퀴즈 풀기 (준비 중)")
        elif choice == 2:
            print("퀴즈 추가 (준비 중)")
        elif choice == 3:
            print("퀴즈 목록 (준비 중)")
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


if __name__ == "__main__":
    main()


