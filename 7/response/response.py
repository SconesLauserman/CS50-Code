from validator_collection import email as email_validator


def main():
    print(validate(input("What's your email adress? ")))


def validate(email):
    try:
        email_validator(email)
        return "Valid"
    except Exception:
        return "Invalid"


if __name__ == "__main__":
    main()
