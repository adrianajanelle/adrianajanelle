"Desired Total Volume to Freeze"


def parse_scientific_input(input_str):
    parts = input_str.split("x10^")
    if len(parts) != 2:
        raise ValueError(
            "Invalid input format. Please enter in the format 'number x10^exponent'")
    number_str, exponent_str = parts
    number = float(number_str)
    exponent = int(exponent_str)
    return number * 10**exponent


def calculate_freeze_volume(tnc):
    freeze_volume = tnc / (4 * 10**8)
    return round(freeze_volume)


def main():
    print("FREEZE VOLUME CALCULATOR")
    tnc_input = input("Enter TNC in scientific notation (e.g., 12.2x10^10): ")
    try:
        tnc = parse_scientific_input(tnc_input)
        freeze_vol = calculate_freeze_volume(tnc)
        print("Desired Total Volume to Freeze:", freeze_vol)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
