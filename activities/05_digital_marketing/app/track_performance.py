from data import campaigns

def track_performance():
    try:
        campaign_id = int(input("Enter campaign ID: "))
        if campaign_id not in campaigns:
            print("Campaign not found. Please check the campaign ID.")
            return

        impressions = int(input("Enter new impressions: "))
        clicks = int(input("Enter new clicks: "))
        conversions = int(input("Enter new conversions: "))

        campaigns[campaign_id]["impressions"] = impressions
        campaigns[campaign_id]["clicks"] = clicks
        campaigns[campaign_id]["conversions"] = conversions
        print("Campaign performance updated successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for metrics.")
