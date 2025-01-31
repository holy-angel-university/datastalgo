from input_traffic_data import input_traffic_data
from analyze_traffic import analyze_traffic
from optimize_timings import optimize_timings
from generate_report import generate_report

def main():
    print("Welcome to the Traffic Optimization System!")
    
    while True:
        action = input("\nWhat would you like to do? (input/analyze/optimize/report/exit): ").strip().lower()
        
        if action == "input":
            input_traffic_data()
        elif action == "analyze":
            analyze_traffic()
        elif action == "optimize":
            optimize_timings()
        elif action == "report":
            generate_report()
        elif action == "exit":
            print("Thank you for using the Traffic Optimization System!")
            break
        else:
            print("Invalid action. Please choose from: input, analyze, optimize, report, exit.")

if __name__ == "__main__":
    main()