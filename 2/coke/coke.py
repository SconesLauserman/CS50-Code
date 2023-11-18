# ================================================================================================================= #
# Function "main":                                                                                                  #
#   Step 1(main): Make list of all the cents that the machine accepts.                                              #
#   Step 2(main): Make while loop that keeps asking user fore money untill the user give the right amount:          #
#       Step 1(main >> While): Ask user to Insert Coin.                                                             #
#       Step 2(main >> While): Make the following conditions to check if the user inserted a acceptable cent.       #
#           Condition 1(main >> While): If the inserted coin is in the acceptable cents then do the following:      #
#               Step 1(main >> While >> If): Minus the amount due with the inserted coin.                           #
#               Step 2(main >> While >> If): Make if condition to check that the amount due is not less than 0.     #
#                   Step 1(main >> While >> If >> If): Print the amount due.                                        #
#           Condition 2(main >> While): Else then do the following:                                                 #
#               Step 1(main >> While): Print the amount due.                                                        #
#   Step 3(main): When the while loop becomes false return and print the amount the costumer is owed.               #
# ================================================================================================================= #


def main(amount_due=50):
    # Step 1(main): Make array of all the cents that the machine accepts.
    acceptable_cents = [5, 10, 25, 50]

    # Step 2(main): Make while loop that keeps going while amount_due is greater than 0:
    while amount_due > 0:
        # Step 1(main >> While): Ask user to "Insert Coin: ".
        insert_coin = int(input("Insert Coin: "))

        # Condition 1(main >> While): If the inserted coin is in the acceptable cent then do the following:
        if insert_coin in acceptable_cents:
            # Step 1(main >> While >> If): Minus the amount_due with the Inserted Coin.
            amount_due -= float(insert_coin)
            # Step 2(main >> While >> If): If the amount_due is less than or equal to 0 then do the following:
            if not amount_due <= 0:
                # Step 1(main >> While >> If >> If): Print "Amount Due: " and then the amount due.
                print(f"Amount Due: {int(amount_due)}")
        # Condtiion 2(main >> While): Else then do the following:
        else:
            # Step 1(main >> While): Print "Amount Due: " and then the amount_due.
            print(f"Amount Due: {int(amount_due)}")
    # Step 3(main): Return "Change Owed: " and then the amount_due as int.
    return print(f"Change Owed: {int(amount_due)}".replace("-", ""))


if __name__ == "__main__":
    main()
