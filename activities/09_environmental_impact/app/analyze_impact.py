from data import environmental_data

def analyze_impact():
    if not environmental_data:
        print("No data found. Please input data first.")
        return
    
    highest_carbon = max(environmental_data, key=lambda k: environmental_data[k]["carbon_emissions"])
    highest_energy = max(environmental_data, key=lambda k: environmental_data[k]["energy_usage"])
    highest_waste = max(environmental_data, key=lambda k: environmental_data[k]["waste_production"])
    
    print("\nEnvironmental Impact Analysis:")
    print(f"- Highest Carbon Footprint: {highest_carbon} ({environmental_data[highest_carbon]['carbon_emissions']} tons)")
    print(f"- Highest Energy Usage: {highest_energy} ({environmental_data[highest_energy]['energy_usage']} kWh)")
    print(f"- Highest Waste Production: {highest_waste} ({environmental_data[highest_waste]['waste_production']} kg)")