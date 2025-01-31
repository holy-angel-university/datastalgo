from data import clients, campaigns

def create_campaign():
    try:
        campaign_id = int(input("Enter campaign ID: "))
        if campaign_id in campaigns:
            print("Campaign ID already exists. Please choose a different ID.")
            return

        client_id = int(input("Enter client ID: "))
        if client_id not in clients:
            print("Client not found. Please check the client ID.")
            return

        name = input("Enter campaign name: ")
        impressions = int(input("Enter initial impressions: "))
        clicks = int(input("Enter initial clicks: "))
        conversions = int(input("Enter initial conversions: "))

        campaigns[campaign_id] = {
            "client_id": client_id,
            "name": name,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions
        }
        print("Campaign created successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for IDs and metrics.")
