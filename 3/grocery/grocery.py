import sys


def main():
    grocery_list = {}
    try:
        while True:
            grocery = input().lower()
            if grocery in grocery_list:
                grocery_list[grocery] = grocery_list[grocery] + 1
            else:
                grocery_list[grocery] = 1
    except EOFError:
        sorted_list = sort_list(grocery_list)
        output = ''
        for i in range(len(sorted_list[0])):
            output += f'{sorted_list[0][i]} {sorted_list[1][i].upper()}\n'
        return print(output)


def sort_list(list=None):
    amount_items = []
    names_items = []
    for grocery, amount in list.items():
        names_items.append(grocery)
        amount_items.append(amount)
    sorted_array = sorted(names_items)
    return [amount_items, sorted_array]


if __name__ == "__main__":
    main()
