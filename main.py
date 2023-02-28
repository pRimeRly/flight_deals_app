from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY = input("Enter origin city IATA CODE eg: 'AMS', 'LON': ")
dataManager = DataManager()
flightSearch = FlightSearch()
notification_manager = NotificationManager()

sheet_data = dataManager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flightSearch.get_destination_code(row["city"])
    dataManager.update_destination_data()

dataManager.destination_data = sheet_data

tomorrow = datetime.now().date() + timedelta(days=1)
six_months_later = tomorrow + timedelta(days=180)

for row in sheet_data:
    flight = flightSearch.search_flights(departure_city_code=ORIGIN_CITY,
                                         arrival_city_code=row["iataCode"],
                                         from_time=tomorrow,
                                         to_time=six_months_later)

    if flight is None:
        continue

    if flight.price < row["lowestPrice"]:
        print("FLight found")

        users = dataManager.get_customer_details()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from " \
                  f"{flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-" \
                  f"{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.nl/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(user_emails=emails, message=message, flight_link=link)
