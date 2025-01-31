from input_data import input_data
from analyze_impact import analyze_impact
from optimize_usage import optimize_usage
from provide_recommendations import provide_recommendations

def main():
    print("Welcome to the Environmental Impact Analysis and Optimization System!")
    
    while True:
        action = input("\nWhat would you like to do? (input/analyze/optimize/recommend/exit): ").strip().lower()
        
        if action == "input":
            input_data()
        elif action == "analyze":
            analyze_impact()
        elif action == "optimize":
            optimize_usage()
        elif action == "recommend":
            provide_recommendations()
        elif action == "exit":
            print("Thank you for using the Environmental Impact Analysis and Optimization System!")
            break
        else:
            print("Invalid action. Please choose from: input, analyze, optimize, recommend, exit.")

if __name__ == "__main__":
    main()