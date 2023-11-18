# =================================================================================================================== #
# Step 1: Make the two functions "dollars_to_float" and "percent_to_float" able to convert to float.                  #
#   Step 1(dollars_to_float): Return dollars as float with the replacement of "$" to ""                               #
#   Step 1(percent_to_float): Return percent as float with the replacement of "%" to ""                               #
# Step 2: In the main function, modify the calculation to get the tip.                                                #
# =================================================================================================================== #


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Step 2: Modify the calculation to be able to calculate the tip, with the adjustment of placing the / 100.
    tip = dollars / 100 * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Steb 1(dollars_to_float): Returning the dollars as float with the replacement of "$" to ""
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Steb 1(percent_to_float): Return the percent as float with the replacement of "%" to ""
    return float(p.replace("%", ""))


main()
