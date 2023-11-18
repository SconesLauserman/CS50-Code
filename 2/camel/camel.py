# ============================================================================================================================================================= #
# Function "main":
#   Step 1(main): Print users camelCase as snake_case using the function "convert_to_snake_case".                                                               #
# Function "convert_to_snake_case":                                                                                                                             #
#   Step 1(convert_to_snake_case): List all the camelCase charakter as an array.                                                                                #
#   Step 2(convert_to_snake_case): For loop thru all the charakter in the camelCase array.                                                                      #
#   Step 3(convert_to_snake_case >> ForLoop): Write the conditionals from what should happen according to what kind of charakter it is:                         #
#       Condition 1(convert_to_snake_case >> ForLoop): If the charakter is upper case then output should be += by "_" and the original letter in lower case.    #
#       Condition 2(convert_to_snake_case >> ForLoop): Else then output should be += by the original letter.                                                    #
#   Step 4(convert_to_snake_case): Return the output.                                                                                                           #
# ============================================================================================================================================================= #


def main():
    # Step 1(main): Print user camelCase as snake_case using the function "convert_to_snake_case".
    print(convert_to_snake_case(input("camelCase: ")))


def convert_to_snake_case(camelCase):
    # Step 1(convert_to_snake_case): List all the charakters in the camelCase.
    camelCase_list = list(camelCase)
    output = ""
    # Step 2(convert_to_snake_case): For loop thru all the charakter in the camelCase:
    for char in camelCase_list:
        # Step 3(convert_to_snake_case >> ForLoop): Write the conditionels from what should happen according to what kind of charakter it is:

        # Condition 1(convert_to_snake_case >> ForLoop): If the charakter isupper() then output should be += by "_" and char.lower().
        if char.isupper():
            output += "_" + char.lower()
        # Condition 2(convert_to_snake_case >> ForLoop): Else then output should be += by char.
        else:
            output += char
    # Step 4(convert_to_snake_case): Return the output.
    return output


if __name__ == "__main__":
    main()
