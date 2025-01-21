def create_conversion_dictionaries():
    meters_to_centimeters = {}
    centimeters_to_meters = {}
    
    for i in range(1, 101):  # Example range from 1 to 100
        meters_to_centimeters[i] = i * 100
        centimeters_to_meters[i * 100] = i
    
    return meters_to_centimeters, centimeters_to_meters

# Create the dictionaries
meters_to_centimeters, centimeters_to_meters = create_conversion_dictionaries()

# Example usage
print("Meters to Centimeters:", meters_to_centimeters)
print("Centimeters to Meters:", centimeters_to_meters)