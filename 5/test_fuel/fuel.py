def main():
    try:
        fraction = convert(input("Fracction: "))
        result = gauge(fraction)
    except Exception:
        return main()
    print(result)


def convert(fraction):
    first_number, second_number = fraction.split("/")
    fraction_eval = int(round(float(first_number) / float(second_number) * 100))
    if fraction_eval <= 0:
        raise ZeroDivisionError
    return fraction_eval


def gauge(percentage):
    if float(percentage) >= 99:
        return "F"
    elif float(percentage) <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
