from sys import argv, exit
from csv import DictReader, DictWriter

try:
    with open(argv[1], "r") as data:
        data_dict = DictReader(data)
        dict = []
        for line in data_dict:
            temp = {}
            last, first = line["name"].split(",")
            temp["first"] = first.strip()
            temp["last"] = last.strip()
            temp["house"] = line["house"]
            dict.append(temp)
    fieldnames = ["first", "last", "house"]
    with open(argv[2], "w", newline="") as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(dict)
except FileNotFoundError:
    print("File was not found")
    exit(1)
