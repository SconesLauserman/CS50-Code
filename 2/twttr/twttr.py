# =========================================================================================================================== #
# Function "main":                                                                                                            #
#   Step 1(main): Print the input of user with the replacements of A, E, I, O and U using the function "replace".             #
# Function "replace":                                                                                                         #
#   Step 2(replace): Make a list of all the charakter that should be replaced.                                                #
#   Step 3(replace): Make a For loop thru all the charakters that should be replaced:                                         #
#       Step 1(replace >> ForLoop): Replace the charakters that should be replaced.                                           #
#   Step 4(replace): Return the output.                                                                                       #
# =========================================================================================================================== #


def main():
    # Step 1(main): Print the input of user with the replacements of A, E, I, O and U using the function "replace".
    print(replace(input("Input: ")))


def replace(sentence):
    # Step 2(replace): Make a list of all the charakters that should be replaced.
    replacements = list("aeiouAEIOU")
    output = sentence
    # Step 3(replace): Make a For Loop thru all the charakters that should be replaced:
    for char in replacements:
        # Steb 1(replace >> ForLoop): replace the charakters that should be replaced.
        output = output.replace(char, "")
    # Step 4(replace): Return the output.
    return f"Output: {output}"


if __name__ == "__main__":
    main()
