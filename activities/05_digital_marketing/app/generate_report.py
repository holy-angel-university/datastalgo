from data import campaigns

def generate_report():
    try:
        campaign_id = int(input("Enter campaign ID: "))
        if campaign_id not in campaigns:
            print("Campaign not found. Please check the campaign ID.")
            return

        campaign = campaigns[campaign_id]
        print("\nCampaign Report:")
        print(f"- Campaign Name: {campaign['name']}")
        print(f"- Impressions: {campaign['impressions']}")
        print(f"- Clicks: {campaign['clicks']}")
        print(f"- Conversions: {campaign['conversions']}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the campaign ID.")
