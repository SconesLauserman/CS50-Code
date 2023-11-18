# ============================================================================================================================================================ #
# Step 1: Within the function "main" Print how much the costumer gets accourding to the greeting using the function "money_from_greeting".                     #
# Step 2: Implement the function "money_from_greeting".                                                                                                        #
# Step 3: Make the conditions in the "money_from_greeting" function:                                                                                           #
#   Condition 1(money_from_greeting): If it is equal to "Hello, Newman" or equal "Hello" then the costumer gets "$0".                                          #
#   Condition 2(money_from_greeting): Else if it is equal to "How you doing?" or equal to "How's it going" then the costumer gets "$20".                       #
#   Condition 3(money_from_greeting): Else then the costumer getes "$100".                                                                                     #
# ============================================================================================================================================================ #


def main():
    # Step 1: Print how much the costumer gets according to the greeting, using the function "money_from_greeting".
    print(money_from_greeting(input("Greeting: ")))


# Step 2: Implement the function "money_from_greeting".
def money_from_greeting(greeting):
    # Step 3: Make the conditions for what the costumer gets according to the greeting:

    greeting_modified = greeting.strip()

    # Condition 1: If the costumer is Greetted with "Hello, Newman" or "Hello" then the costumer gets "$0":
    if greeting_modified == "Hello, Newman" or greeting_modified == "Hello":
        return "$0"
    # Condition 2: If the cosrumer is greetted with "How you doing?" or "How's it going?" then the costumer gets "$20":
    elif (
        greeting_modified == "How you doing?" or greeting_modified == "How's it going?"
    ):
        return "$20"
    # Condition 3: Eles the costumer gets "$100":
    else:
        return "$100"


if __name__ == "__main__":
    main()
