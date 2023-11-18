import inflect

p = inflect.engine()
people = []
try:
    while True:
        people.append(input("Name: "))
except EOFError:
    print("Adieu, adieu, to " + p.join(people))
