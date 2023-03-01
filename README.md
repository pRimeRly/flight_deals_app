# Flight Deal App

This project is a Python-based application designed to provide email alerts for the best flight deals from a user-specified departure city. 
The application integrates with the Sheety API to facilitate data transfer between Google Sheets and the program, enabling the storage and retrieval of destination data. 
The Kiwi Flight Search API is used to search for the cheapest flight deals available.
By leveraging these powerful APIs and the search criteria specified by the user the program will scour the Kiwi Flight Search API to find the most cost-effective flight deals available. 
If a desirable deal is identified, the program will promptly send an email alert to the user, notifying them of the deal's availability.

## Features
* Finds the cheapest flight deals from a given city for the next six months
* Sends email alerts to customers when a flight deal is found
* Stores and accesses destination data using the Sheety API
* Searches for flights using the Kiwi Flight Search API


## Prerequisites
* Python 3.x
* Google Sheet API credentials
* Tequila API credentials

## How to Use
1. Clone this repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.
3. Replace TEQUILA_API_KEY with your Kiwi Flight Search API key in the flight_search.py file.
4. Replace YOUR_SHEETY_ENDPOINT and YOUR_SHEETY_TOKEN with your own values in the data_manager.py file.
5. Add destination data to the Google Sheets document linked in the YOUR_SHEETY_ENDPOINT endpoint in the format specified in the document (Code automatically fills in the IATA codes).

![image](https://user-images.githubusercontent.com/99833317/222012174-8ac4fedc-1977-453a-9791-eb523a151b54.png)

![image](https://user-images.githubusercontent.com/99833317/222012602-9d058717-a1f0-4613-b449-8c54e73154e7.png)
> ![image](https://user-images.githubusercontent.com/99833317/222012733-c9d7d09c-3ad7-4a40-933d-32e57b97afa6.png)


6. Run the program using python main.py.
7. Enter the origin city IATA CODE when prompted, e.g. 'AMS', 'LON'.

## How it Works
```
When the program is run, the user is prompted to enter the origin city IATA CODE.
The program retrieves the destination data from the Google Sheets document linked in the YOUR_SHEETY_ENDPOINT endpoint using the Sheety API.
If the IATA CODE for a destination is not provided in the sheet, the program uses the Kiwi Flight Search API to retrieve the IATA CODE and updates the sheet.
The program then searches for flights from the origin city to each destination in the sheet using the Kiwi Flight Search API.
If a flight deal is found that is cheaper than the lowest price in the sheet, an email alert is sent to all customers in the sheet using the Notification Manager.
The email alert includes the details of the flight deal and a link to book the flight.
```
