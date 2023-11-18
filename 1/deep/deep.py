# ================================================================================================================================== #
# Step 1: Within the function "main" Print "Yes" if the users answer were correct and, else "No" using the function "is_correct".    #
# Step 2: Implement the function "is_correct".                                                                                       #
# Step 3: Make the conditions fore the function "is_correct":                                                                        #
#   Condition 1(is_correct): If the users answer is "42", "Forty Two" or "forty-two" then return "Yes".                              #
#   Condition 2(is_correct): If the user does not answer any of the specified answers then return "No".                              #
# ================================================================================================================================== #


def main():
    # Step 1: Print "Yes" if the user answer correct to the question and "No" if not, using the function "is_correct".
    print(
        is_correct(
            input(
                "What is the Answer to the Great Question of Life, the Universe, and Everything? "
            )
        )
    )


# Step 2: Implement the function "is_correct":
def is_correct(answer):
    # Step 3(is_correct): Make the conditions fore the function "is_correct":

    answer_modified = answer.lower().strip()

    # Condition 1(is_correct): If the users answer is "42", "Forty Two" or "forty-two" then return "Yes":
    if (
        answer_modified == "42"
        or answer_modified == "forty two"
        or answer_modified == "forty-two"
    ):
        return "Yes"
    # Condition 2(is_correct): If the users answer was none of the ones specified then return "No":
    else:
        return "No"


if __name__ == "__main__":
    main()
