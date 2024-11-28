import pandas as pd

hotel_df = pd.read_csv("hotels.csv")


class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id
        pass

    def book(self):
        pass

    def available(self):
        pass

class ReservationTicket:
    def __init__(self, cust_name, hotel_id):
        self.name = name
        self.hotel_id = hotel_id
        pass

    def generate(self):
        pass


print(hotel_df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
else:
    print("Hotel is not available")