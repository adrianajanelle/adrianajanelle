def calculate_freezing_media_volume(desired_volume):
    return desired_volume * 0.10

# Example usage
desired_total_volume_to_freeze = float(input("Enter Desired Total Volume to Freeze (mL): "))
freezing_media_volume = calculate_freezing_media_volume(desired_total_volume_to_freeze)
print(f"Freezing media Volume: {freezing_media_volume:.2f} mL")
