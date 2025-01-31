from add_product import add_product
from record_sale import record_sale
from view_inventory import view_inventory
from calculate_revenue import calculate_revenue
from analyze_performance import analyze_performance

def main():
    print("Welcome to the Real-Time Sales Tracking System!")

    while True:
        action = input("\nWhat would you like to do? (add/record/view/revenue/analyze/exit): ").strip().lower()

        if action == "add":
            add_product()
        elif action == "record":
            record_sale()
        elif action == "view":
            view_inventory()
        elif action == "revenue":
            calculate_revenue()
        elif action == "analyze":
            analyze_performance()
        elif action == "exit":
            print("Thank you for using the Real-Time Sales Tracking System!")
            break
        else:
            print("Invalid action. Please choose from: add, record, view, revenue, analyze, exit.")

if __name__ == "__main__":
    main()
