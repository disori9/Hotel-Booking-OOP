import pandas as pd

hotel_df = pd.read_csv("hotels.csv")

class Hotel:
    def __init__(self, id):
        self.id = id
        pass

    def book(self):
        pass

    def available(self):
        pass

class ReservationTicket:
    def __init__(self, name, hotel):
        self.name = name
        self.hotel = hotel
        pass

    def generate(self):
        pass


print(hotel_df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)