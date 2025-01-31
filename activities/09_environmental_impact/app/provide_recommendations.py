from data import environmental_data

def provide_recommendations():
    if not environmental_data:
        print("No data found. Please input data first.")
        return
    
    activity = input("Enter activity name for recommendations: ")
    if activity not in environmental_data:
        print("Activity not found. Please check the activity name.")
        return
    
    print(f"\nRecommendations for {activity}:")
    print("1. Switch to renewable energy sources (e.g., solar panels).")
    print("2. Implement a recycling program to reduce waste production.")
    print("3. Use energy-efficient appliances to lower energy consumption.")