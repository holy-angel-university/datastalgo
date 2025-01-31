from data import flights

def add_flight():
    try:
        flight_number = int(input("Enter flight number: "))
        if flight_number in flights:
            print("Flight number already exists. Please choose a different number.")
            return
        
        destination = input("Enter destination: ")
        seat_capacity = int(input("Enter seat capacity: "))
        
        flights[flight_number] = {
            "destination": destination,
            "seat_capacity": seat_capacity,
            "booked_seats": 0,
            "passengers": []
        }
        print("Flight added successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for flight number and seat capacity.")