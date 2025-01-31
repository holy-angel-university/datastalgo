from data import environmental_data

def optimize_usage():
    if not environmental_data:
        print("No data found. Please input data first.")
        return
    
    activity = input("Enter activity name to optimize: ")
    if activity not in environmental_data:
        print("Activity not found. Please check the activity name.")
        return
    
    data = environmental_data[activity]
    optimized_energy = data["energy_usage"] * 0.8  # Reduce energy usage by 20%
    optimized_waste = data["waste_production"] * 0.7  # Reduce waste by 30%
    
    print(f"\nOptimized Resource Usage for {activity}:")
    print(f"- Reduce energy usage by 20% ({optimized_energy:.2f} kWh).")
    print(f"- Increase recycling rate by 30% (waste reduced to {optimized_waste:.2f} kg).")