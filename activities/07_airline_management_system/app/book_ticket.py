from data import flights

def book_ticket():
    try:
        flight_number = int(input("Enter flight number: "))
        if flight_number not in flights:
            print("Flight not found. Please check the flight number.")
            return
        
        if flights[flight_number]["booked_seats"] >= flights[flight_number]["seat_capacity"]:
            print("No available seats. Flight is fully booked.")
            return
        
        passenger_name = input("Enter passenger name: ")
        seat_number = flights[flight_number]["booked_seats"] + 1
        flights[flight_number]["booked_seats"] += 1
        flights[flight_number]["passengers"].append({"name": passenger_name, "seat": seat_number})
        print(f"Ticket booked successfully! Seat number: {seat_number}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")