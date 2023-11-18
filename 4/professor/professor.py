import random


def main():
    try:
        amount_correct = 0
        try:
            level = get_level()
        except Exception:
            return main()
        amount_wrong_in_a_row = 0
        wrong_question = ""
        wrong_question_answer = 0
        times_to_run = 10
        i = 1
        while i <= times_to_run:
            if amount_wrong_in_a_row <= 0:
                try:
                    x = generate_integer(level)
                    y = generate_integer(level)
                except Exception:
                    pass
                user_answer = input(f"{x} + {y} = ")
            else:
                if amount_wrong_in_a_row >= 3:
                    print(f"{wrong_question}{wrong_question_answer}")
                    amount_wrong_in_a_row = 0
                    i += 1
                    continue
                else:
                    user_answer = input(wrong_question)
            if int(user_answer) == x + y:
                amount_correct += 1
                i += 1
                print("correct")
                amount_wrong_in_a_row = 0
            else:
                print("EEE")
                amount_wrong_in_a_row += 1
                wrong_question = f"{x} + {y} = "
                wrong_question_answer = x + y
    except Exception:
        pass
    print(f"Score: {amount_correct}")


def get_level():
    level = input("Level: ")
    if level in ["1", "2", "3"]:
        return level
    else:
        return get_level()


def generate_integer(level):
    if level in ["1", "2", "3"]:
        random_range_x = "1"
        random_range_y = "9"
        if level == "1":
            random_range_x = "0"
        for i in range(int(level) - 1):
            random_range_x += "0"
            random_range_y += "9"
        return random.randint(int(random_range_x), int(random_range_y))
    else:
        raise ValueError


if __name__ == "__main__":
    main()
