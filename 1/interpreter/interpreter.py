# =========================================================================================================================================== #
# Step 1: Within the function "main" Print the answer to the user math expression. Calculate using the function "interpreter".                #
# Step 2: Implement the function "interpreter".                                                                                               #
# Step 3: Write the function "interpreter":                                                                                                   #
#   Step 1(interpreter): Split the expression into 3 parts: first_number, operator and second_number.                                         #
#   Step 2(interpreter): Make the right conditionals to how the calculation should be performed out for which operator the user chose:        #
#       Condition 1(interpreter): If the operator is equal to "+" then return first_number + second_number.                                   #
#       Condition 2(interpreter): If the operator is equal to "-" then return first_number - second_number.                                   #
#       Condition 3(interpreter): If the operator is equal to "*" then return first_number * second_number.                                   #
#       Condition 4(interpreter): If the operator is equal to "/" then return first_number / second_number.                                   #
# =========================================================================================================================================== #


def main():
    # Step 1: Print the answer to the users math expression. Calculate using the function "interpreter".
    print(interpreter(input("Expression: ").split(" ")))


# Step 2: Implement the function "interpreter".
def interpreter(expression):
    # Step 1(interpreter): Split the expression into 3 parts: fist_number, operator and second_number.
    first_number, operator, second_number = expression

    # Step 2(interpreter): Make the right conditionels to how the calculation should be performed out for which operator the user chose:

    # Condition 1(interpreter): If the operator is equal to "+" then return first_number + second_number.
    if operator == "+":
        return float(first_number) + float(second_number)

    # Condition 2(interpreter): If the operator is equal to "-" then return first_number - second_number.
    elif operator == "-":
        return float(first_number) - float(second_number)

    # Condition 3(interpreter): If the operator is equal to "*" then return first_number * second_number.
    elif operator == "*":
        return float(first_number) * float(second_number)

    # Condition 4(interpreter): If the operator is equal to "/" then return first_number / second_number.
    elif operator == "/":
        return float(first_number) / float(second_number)


if __name__ == "__main__":
    main()
