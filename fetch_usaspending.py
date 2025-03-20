import requests
import json

# API endpoint
#TSCTI TEST
url = "https://api.usaspending.gov/api/v2/recipient/children/028619588"

def fetch_usaspending_data():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse JSON response
        data = response.json()

        # Save data to a JSON file
        with open("usaspending_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data successfully fetched and saved to usaspending_data.json.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_usaspending_data()
