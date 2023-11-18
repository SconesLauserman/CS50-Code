import random

correct_number = 0
number = 9999999

was_valid = False

message = "Level: "
level = 0
while number != correct_number:
    try:
        user = int(input(message))
        was_valid = True
    except ValueError:
        user = int(input(message))
    if message == "Level: ":
        if not user < 1:
            correct_number = random.randint(0, user)
            level = user
            message = "Guess: "

    else:
        if was_valid:
            number = user
            if number > level:
                pass
            elif number < correct_number:
                print("Too small!")
            elif number > correct_number:
                print("Too large!")
            else:
                
                print("Just right!")
                break
