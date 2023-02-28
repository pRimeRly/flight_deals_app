import os
import requests

SHEETY_URL = "https://sheety.co/docs"
API_AUTH_KEY = os.environ["SHEETY_AUTH_KEY"]
API_KEY_STRING = "Authorization"
api_headers = {
    API_KEY_STRING: API_AUTH_KEY
}

# endpoints gotten after tracking sheets document with the sheety api
flight_deals_endpoint = "YOUR ENDPOINT FROM SHEETY CONSOLE"
customer_details_endpoint = "https://api.sheety.co/d690dfc33ceab01ddbcddb1f13148da7/flightDeals/users"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=flight_deals_endpoint, headers=api_headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for row in self.destination_data:
            json_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            row_id = row["id"]
            response = requests.put(
                url=f"{flight_deals_endpoint}/{row_id}",
                headers=api_headers,
                json=json_data
            )
            response.raise_for_status()
            print(response.text)
    def get_customer_details(self):
        response = requests.get(url=customer_details_endpoint, headers=api_headers)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
