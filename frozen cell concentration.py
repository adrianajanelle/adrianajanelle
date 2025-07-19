def calculate_frozen_cell_concentration():
    try:
        tnc_input = input("Enter TNC in scientific notation (e.g., 12.2x10^10): ")
        tnc = parse_scientific_input(tnc_input)
        desired_volume = float(input("Enter Desired Volume to Freeze: "))
        frozen_cell_concentration = tnc / desired_volume
        result = frozen_cell_concentration / (10**8)
        print(f"Frozen Cell Concentration (<=4x10^8 cells/mL): {result} x10^8")
    except ValueError as e:
        print("Error:", e)

def parse_scientific_input(input_str):
    parts = input_str.split("x10^")
    if len(parts) != 2:
        raise ValueError(
            "Invalid input format. Please enter in the format 'number x10^exponent'")
    number_str, exponent_str = parts
    number = float(number_str)
    exponent = int(exponent_str)
    return number * 10**exponent

calculate_frozen_cell_concentration()

