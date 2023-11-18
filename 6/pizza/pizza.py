from tabulate import tabulate
from csv import reader
import sys


if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif sys.argv[1].split(".")[1] != "csv":
    print("Not a csv file")
    sys.exit(1)

menu_data = []


try:
    with open(sys.argv[1], "r") as csv:
        csv_readed = reader(csv)
        for line in csv_readed:
            menu_data.append(line)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
print(tabulate(menu_data, headers="firstrow", tablefmt="grid"))
