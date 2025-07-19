def calculate_dmso_volume(desired_total_volume_to_freeze):
    dmso_volume = desired_total_volume_to_freeze * 0.10
    return dmso_volume

# Example usage
desired_total_volume_to_freeze = float(input("Enter the desired total volume to freeze in mL: "))
dmso_volume = calculate_dmso_volume(desired_total_volume_to_freeze)
print(f"DMSO Volume: {dmso_volume} mL")
