from add_flight import add_flight
from book_ticket import book_ticket
from view_flight import view_flight
from generate_report import generate_report

def main():
    print("Welcome to the Airlines Management System!")
    
    while True:
        action = input("\nWhat would you like to do? (add/book/view/report/exit): ").strip().lower()
        
        if action == "add":
            add_flight()
        elif action == "book":
            book_ticket()
        elif action == "view":
            view_flight()
        elif action == "report":
            generate_report()
        elif action == "exit":
            print("Thank you for using the Airlines Management System!")
            break
        else:
            print("Invalid action. Please choose from: add, book, view, report, exit.")

if __name__ == "__main__":
    main()