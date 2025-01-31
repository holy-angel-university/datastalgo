from data import flights

def generate_report():
    try:
        flight_number = int(input("Enter flight number: "))
        if flight_number not in flights:
            print("Flight not found. Please check the flight number.")
            return
        
        flight = flights[flight_number]
        revenue = flight["booked_seats"] * 200  # Assuming $200 per ticket
        print("\nFlight Report:")
        print(f"- Destination: {flight['destination']}")
        print(f"- Total Seats: {flight['seat_capacity']}")
        print(f"- Booked Seats: {flight['booked_seats']}")
        print(f"- Available Seats: {flight['seat_capacity'] - flight['booked_seats']}")
        print(f"- Revenue: ${revenue:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")