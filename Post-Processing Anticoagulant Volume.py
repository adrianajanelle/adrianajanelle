"Post-Processing Anticoagulant Volume"


def calculate_post_processing_anticoagulant_volume(pre_anticoag_volume, post_corrected_volume, pre_corrected_volume):
    post_anticoag_volume = (pre_anticoag_volume *
                            post_corrected_volume) / pre_corrected_volume
    return post_anticoag_volume


def main():
    print("POST PROCESSING ANTICOAGULANT VOLUME CALCULATOR")
    pre_anticoag_volume = float(
        input("Enter Pre-Processing Anticoagulant Volume (mL): "))
    post_corrected_volume = float(
        input("Enter Post-Processing Corrected Product Volume (mL): "))
    pre_corrected_volume = float(
        input("Enter Pre-Processing Corrected Product Volume (mL): "))
    post_anticoag_volume = calculate_post_processing_anticoagulant_volume(
        pre_anticoag_volume, post_corrected_volume, pre_corrected_volume)
    print("Post Processing Anticoagulant Volume:", post_anticoag_volume, "mL")


if __name__ == "__main__":
    main()
