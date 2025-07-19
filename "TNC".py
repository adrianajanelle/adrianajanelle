"TNC"


def calculate_tnc(wbc, corrected_volume):
    tnc = wbc * 10**6 * corrected_volume
    return tnc


def format_tnc(tnc):
    # Adjust TNC to represent in x10^10 format
    tnc_adjusted = tnc / 10**10
    return "{:.2f} x10^10".format(tnc_adjusted)


def main():
    print("TNC CALCULATOR")
    wbc = float(input("Enter WBC count: "))
    corrected_volume = float(input("Enter Corrected Product Volume (mL): "))
    tnc = calculate_tnc(wbc, corrected_volume)
    tnc_formatted = format_tnc(tnc)
    print("TNC:", tnc_formatted)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
