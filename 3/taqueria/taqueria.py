import sys
felipes_taqueria_menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00,
}

total = 0
while True:
    try:
        item_menu = input("Item: ").lower()
        if item_menu in felipes_taqueria_menu:
            total += felipes_taqueria_menu[item_menu]
            print(f"Total: ${total}0")
        else:
            pass
    except EOFError:
        sys.exit(0)
