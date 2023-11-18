# ================================================================================================================== #
# Step 1: Within function "main" Print user message with the right replacements, using the function "convert".       #
# Step 2: Implement the function "convert".                                                                          #
#   Step 1(convert): Return message with replacements of ":(" to "🙁" and ":)" to "🙂".                             #
# ================================================================================================================== #


def main():
    # Step 1: Print user message with the right replacements using the function "convert".
    print(convert(input("")))


# Step 2: Implement the function "convert".
def convert(message):
    # Step 1(convert): Return message with the replacements of ":(" to "🙁" and ":)" to "🙂".
    return message.replace(":)", "🙂").replace(":(", "🙁")


main()
