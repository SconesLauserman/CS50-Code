def main():
    print(value(input("Greeting: ")))


def value(greeting):
    greeting_modified = greeting.lower().strip()
    if greeting_modified.startswith("hello"):
        return 0
    elif greeting_modified.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
