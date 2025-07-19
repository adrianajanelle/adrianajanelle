"Corrected Product Volume"


def calculate_corrected_product_volume(tared_weight):
    corrected_volume = tared_weight / 1.06
    return corrected_volume


def main():
    print("CORRECTED PRODUCT VOLUME CALCULATOR")
    tared_weight = float(input("Enter Tared Product Weight: "))
    corrected_volume = calculate_corrected_product_volume(tared_weight)
    print("Corrected Product Volume:", corrected_volume)


if __name__ == "__main__":
    main()
