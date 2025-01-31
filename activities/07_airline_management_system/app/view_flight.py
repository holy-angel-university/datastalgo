from data import flights

def view_flight():
    try:
        flight_number = int(input("Enter flight number: "))
        if flight_number not in flights:
            print("Flight not found. Please check the flight number.")
            return
        
        flight = flights[flight_number]
        print("\nFlight Details:")
        print(f"- Destination: {flight['destination']}")
        print(f"- Available Seats: {flight['seat_capacity'] - flight['booked_seats']}")
        print("- Passengers:")
        for passenger in flight["passengers"]:
            print(f"  {passenger['name']} (Seat: {passenger['seat']})")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")