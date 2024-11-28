import pandas as pd

hotel_df = pd.read_csv("hotels.csv")


class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id
        pass

    def book(self):
        """Book method that changes availability in the hotel data if it is booked"""
        hotel_df.loc[hotel_df['id'] == self.id]['available'] = 'no'
        hotel_df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = hotel_df.loc[hotel_df['id'] == self.id]['available'].squeeze()
        print(availability)
        if availability == "yes":
            print("available")
            return True
        else:
            print("not available")
            return False

class ReservationTicket:
    def __init__(self, cust_name, hotel_id):
        self.name = name
        self.hotel_id = hotel_id
        pass

    def generate(self):
        pass


print(hotel_df)
hotel_id = int(input("Enter the id of the hotel: "))
hotel = Hotel(hotel_id)

if hotel.available() is True:
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
else:
    print("Hotel is not available")