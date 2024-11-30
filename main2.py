import pandas as pd
from abc import ABC, abstractmethod


hotel_df = pd.read_csv("hotels.csv", dtype={'id': str})


class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id
        pass

    def get_name(self):
        hotel_name = hotel_df.loc[hotel_df['id'] == self.id, 'name'].squeeze()
        return hotel_name

    def book(self):
        """Book method that changes availability in the hotel data if it is booked"""
        hotel_df.loc[hotel_df['id'] == self.id, 'available'] = "no"
        hotel_df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = hotel_df.loc[hotel_df['id'] == self.id, 'available'].squeeze()

        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data_frame):
        return len(data_frame)

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, cust_name, hotel_object):
        self.name = cust_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation
        Here are your booking data:
        Name: {self.name}
        Hotel: {self.hotel.get_name()}"""

        return content

    @property
    def the_customer_name(self):
        name = self.name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2
