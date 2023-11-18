# ========================================================================================================================================= #
# Step 1: Within function "main" Print user input with the white spaces replace with "..." using the "replace_white_space" function.        #
# Step 2: Implement function "replace_white_space".                                                                                         #
#   Step 1(replace_white_space): Return user input with replacement of " " to "...".                                                        #
# ========================================================================================================================================= #


def main():
    # Step 1: Print user input with the white spaces replaced using the "replace_white_space" function:
    print(replace_white_space(input()))


# Step 2: Implement function "replace_white_space":
def replace_white_space(user):
    # Step 1(replace_white_space): Return user input with replacement of " " to "...":
    return user.replace(" ", "...")


main()
