import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif sys.argv[1].split(".")[1] != "py":
    print("Not a python file")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as file:
        if sys.argv[1].split(".")[1] != "py":
            sys.exit()
        amount_lines = 0
        for line in file:
            if line.strip().startswith("#"):
                pass
            elif len(line.strip()) < 1:
                pass
            else:
                amount_lines += 1
        print(amount_lines)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
