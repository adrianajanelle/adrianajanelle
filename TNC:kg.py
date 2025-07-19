"TNC/kg"


def calculate_tnc_per_kg(wbc, corrected_volume, recipient_weight):
    tnc_per_kg = (wbc * 10**6 * corrected_volume) / recipient_weight
    return tnc_per_kg


def format_tnc_per_kg(tnc_per_kg):
    # Adjust TNC per kg to represent in x10^8 format
    tnc_adjusted = tnc_per_kg / (10**8)
    return "{:.1f}".format(tnc_adjusted)


def main():
    print("TNC per kilogram CALCULATOR")
    wbc = float(input("Enter WBC count: "))
    corrected_volume = float(input("Enter Corrected Product Volume (mL): "))
    recipient_weight = float(input("Enter Recipient Weight (kg): "))
    tnc_per_kg = calculate_tnc_per_kg(wbc, corrected_volume, recipient_weight)
    tnc_per_kg_formatted = format_tnc_per_kg(tnc_per_kg)
    print("TNC per kilogram:", tnc_per_kg_formatted)


if __name__ == "__main__":
    main()
