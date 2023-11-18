# ===================================================================================================================================== #
# Step 1: Within function "main" Print user input mass(measured in kilograms) to Energy(measured in jules) using the function "m_to_E"  #
# Step 2: Implement function "m_to_E"                                                                                                   #
#   Step 1(m_to_E): Make variable "light_speed".                                                                                        #
#   Step 2(m_to_E): Make variable "calculation" that uses this calculation - m * light_speed ^ 2.                                       #
#   Step 3(m_to_E): Return calculation.                                                                                                 #
# ===================================================================================================================================== #


def main():
    # Step 1: Print user input mass(measured in kilograms) to Energy(measured in jules) using the function "m_to_E"
    print(m_to_E(input("m: ")))


# Step 2: Implement function "m_to_E":
def m_to_E(m):
    # Step 1(m_to_E): Make variable "light_speed".
    light_speed = 300000000
    # Step 2(m_to_E): Make variable "calculation" that uese the calculation - m * light_speed ^ 2.
    calculation = float(m) * light_speed ** 2
    # Step 3(m_to_E): Return calculation.
    return f"E: {calculation:.0f}"



main()
