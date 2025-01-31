from data import traffic_data

def analyze_traffic():
    try:
        intersection_id = int(input("Enter intersection ID: "))
        if intersection_id not in traffic_data:
            print("No data found for this intersection.")
            return
        
        data = traffic_data[intersection_id]
        time_counts = {}
        
        for entry in data:
            hour = entry["time"].hour
            if hour not in time_counts:
                time_counts[hour] = {"total_cars": 0, "count": 0}
            time_counts[hour]["total_cars"] += entry["cars"]
            time_counts[hour]["count"] += 1
        
        peak_hour = max(time_counts, key=lambda k: time_counts[k]["total_cars"] / time_counts[k]["count"])
        off_peak_hour = min(time_counts, key=lambda k: time_counts[k]["total_cars"] / time_counts[k]["count"])
        
        print(f"\nTraffic Patterns for Intersection {intersection_id}:")
        print(f"- Peak Hours: {peak_hour:02}:00 - {peak_hour + 1:02}:00 (Average Cars: {time_counts[peak_hour]['total_cars'] / time_counts[peak_hour]['count']:.0f})")
        print(f"- Off-Peak Hours: {off_peak_hour:02}:00 - {off_peak_hour + 1:02}:00 (Average Cars: {time_counts[off_peak_hour]['total_cars'] / time_counts[off_peak_hour]['count']:.0f})")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the intersection ID.")