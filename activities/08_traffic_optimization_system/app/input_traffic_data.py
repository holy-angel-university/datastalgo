from datetime import datetime
from data import traffic_data

def input_traffic_data():
    try:
        intersection_id = int(input("Enter intersection ID: "))
        cars = int(input("Enter number of cars: "))
        time_str = input("Enter time (HH:MM): ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        
        time = datetime.strptime(time_str, "%H:%M").time()
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        if intersection_id not in traffic_data:
            traffic_data[intersection_id] = []
        
        traffic_data[intersection_id].append({
            "cars": cars,
            "time": time,
            "date": date
        })
        print("Traffic data recorded successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for intersection ID and number of cars, and valid time/date formats.")