def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    amount_times = 0
    amount_digits = 0
    is_started_checking = False
    plate_list = list(plate)
    if len(plate_list) >= 2 and len(plate_list) <= 6:
        for char in plate_list:
            amount_times += 1

            if not char.isalpha() and not char.isdigit():
                return False
            if amount_times <= 2:
                if char.isdigit():
                    return False
            else:
                if char.isdigit() and not is_started_checking:
                    is_started_checking = True
                if is_started_checking:
                    if amount_digits <= 0:
                        if plate_list[amount_times - 1] == "0":
                            return False
                    amount_digits += 1
                    if char.isalpha():
                        return False
        return True
    return False


if __name__ == "__main__":
    main()
