from data import environmental_data

def input_data():
    try:
        activity = input("Enter activity name: ")
        carbon_emissions = float(input("Enter carbon emissions (in tons): "))
        energy_usage = float(input("Enter energy usage (in kWh): "))
        waste_production = float(input("Enter waste production (in kg): "))
        
        environmental_data[activity] = {
            "carbon_emissions": carbon_emissions,
            "energy_usage": energy_usage,
            "waste_production": waste_production
        }
        print("Environmental data recorded successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for carbon emissions, energy usage, and waste production.")