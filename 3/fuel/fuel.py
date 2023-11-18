def main():
    fraction_to_percent(input("Fraction: "))


def fraction_to_percent(fraction):
    output = ""

    try:
        first_number, second_number = fraction.split("/")
        fraction_eval = int(round(float(first_number) / float(second_number) * 100))
        if int(first_number) > int(second_number):
            return main()
        elif fraction_eval <= 1:
            output = "E"
        elif fraction_eval >= 99:
            output = "F"

        else:
            output = f"{fraction_eval}%"

    except Exception:
        return main()
    return print(output)


if __name__ == "__main__":
    main()
