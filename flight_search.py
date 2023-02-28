import requests
import os
from flight_data import FlightData
from datetime import datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=query)
        results = response.json()["locations"]
        iata_code = results[0]["code"]
        return iata_code

    def search_flights(self, departure_city_code, arrival_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": departure_city_code,
            "fly_to": arrival_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 2
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]

            depart_date = datetime.utcfromtimestamp(data["route"][0]["dTime"])
            return_date = datetime.utcfromtimestamp(data["route"][2]["dTime"])
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=depart_date.date(),
                return_date=return_date.date(),
                stop_overs=query["max_stopovers"],
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            depart_date = datetime.utcfromtimestamp(data["route"][0]["dTime"])
            return_date = datetime.utcfromtimestamp(data["route"][1]["dTime"])
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=depart_date.date(),
                return_date=return_date.date()
            )
            print(f"{flight_data.destination_city}: €{flight_data.price}")
            return flight_data
