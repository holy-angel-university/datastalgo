from data import traffic_data

def optimize_timings():
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
        
        peak_duration = 90  # Default peak duration in seconds
        off_peak_duration = 30  # Default off-peak duration in seconds
        
        print(f"\nOptimized Traffic Light Timings for Intersection {intersection_id}:")
        print(f"- Peak Hours: {peak_hour:02}:00 - {peak_hour + 1:02}:00 (Green Light Duration: {peak_duration} seconds)")
        print(f"- Off-Peak Hours: {off_peak_hour:02}:00 - {off_peak_hour + 1:02}:00 (Green Light Duration: {off_peak_duration} seconds)")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the intersection ID.")