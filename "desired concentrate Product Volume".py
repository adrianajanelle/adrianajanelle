
"desired concentrate Product Volume"


def calculate_concentrate_volume(total_freeze_volume):
    concentrate_volume = total_freeze_volume * 0.70
    return concentrate_volume


def main():
    print("CONCENTRATE VOLUME CALCULATOR")
    total_freeze_vol = float(
        input("Enter Desired Total Volume to Freeze (mL): "))
    concentrate_vol = calculate_concentrate_volume(total_freeze_vol)
    print("Desired Concentrate Product Volume:", concentrate_vol, "mL")


if __name__ == "__main__":
    main()
