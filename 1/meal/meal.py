# ============================================================================================================================================ #
# Step 1: Within the function "main" Print what time it is according to the users time, do this using the function "convert".                  #
# Step 2: Implement the function "convert".                                                                                                    #
# Step 3: Write the function "convert":                                                                                                        #
#   Step 1(convert): Get the hours and minutes of array "time".                                                                                #
#   Step 2(convert): Make the calculation to get the 24 hour format time.                                                                      #
#   Step 3(convert): Return the calculation.                                                                                                   #
# Step 4(main): Write the right conditionals to know which time it is:                                                                         #
#   Condition 1(main): If the time is between 07:00 and 08:00 then return "breakfast time".                                                    #
#   Condition 2(main): Else if the time is between 12:00 and 13:00 then return "lunch time".                                                   #
#   Condition 3(main): Else if the time is between 18:00 and 19:00 then return "dinner time".                                                  #
#   Condition 4(main): Else then return nothing.                                                                                               #
# ============================================================================================================================================ #


def main():
    # Step 1: Print what time it is according to the users input, using the function "convert".
    time = convert(input("What time is it? "))
    # Step 4(main): Write the conditionals to know which time it is:

    # Condition 1(main): If the time is between 07:00 and 08:00 then return "breakfast time".
    if float(time) >= 7.0 and float(time) <= 8.0:
        return print("breakfast time")
    # Condition 2(main): Else if the time is between 12:00 and 13:00 then return "lunch time".
    elif float(time) >= 12.0 and float(time) <= 13.0:
        return print("lunch time")
    # Condition 3(main): Else if the time is between 18:00 and 19:00 then return "dinner time".
    elif float(time) >= 18.0 and float(time) <= 19.0:
        return print("dinner time")
    # Condition 4(main): Else then return nothing.
    else:
        return


# Step 2: Implement the function "convert".
def convert(time):
    # Step 1(convert): Get the hours and minutes from the array "time".
    hours, minuttes = time.split(":")
    # Step 2(convert): Make the calculation to get the 24 hour format time.
    calculate = float(hours) + float(minuttes) / 60
    # Step 3(convert): Return the calculation
    return f"{calculate}"


if __name__ == "__main__":
    main()
