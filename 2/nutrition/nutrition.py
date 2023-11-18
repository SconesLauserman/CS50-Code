# ====================================================================================================== #
# Step 1: Make a dictanary of fruit as the key and calories as the value.                                #
# Step 2(main): Ask user fore Item.                                                                      #
# Step 3(main): Making the conditionels to make the right responds to what the user typed:               #
#   Condition 1(main): If the fruit is within the dictanary then print the amount of calories.           #
#   Condition 2(main): If the fruit is not within the dictanary then print "Food is not recodnised".     #
# ====================================================================================================== #


# Step 1: Make a dictanary of fruit as the key and calories as the value.
fruit_to_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


def main():
    # Step 1: Ask user fore Item.
    fruit = input("Item: ").lower()

    # Step 3: Make the right conditionels to give the right responds:

    # Condition 1: If the fruit is in the dictanary then print the amount of calories is within the fruit.
    if fruit in fruit_to_calories:
        print(f"Calories: {fruit_to_calories[fruit]}")
    # Condition 2: Uf tge fruit is not in the dictanary then print "Food is not recodnised"
    else:
        print("")


if __name__ == "__main__":
    main()
