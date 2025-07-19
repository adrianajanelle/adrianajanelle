def calculate_plasma_lyte_a_volume(desired_volume):
    return desired_volume * 0.20

desired_volume = float(input("Enter the Desired Total Volume to Freeze in mL: "))
plasma_lyte_a_volume = calculate_plasma_lyte_a_volume(desired_volume)
print(f"The Plasma-Lyte A volume is: {plasma_lyte_a_volume} mL")
