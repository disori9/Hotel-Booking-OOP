import pandas as pd

hotel_df = pd.read_csv("hotels.csv")


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

class ReservationTicket:
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

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvc, holder):
        cc_df = pd.read_csv("cards.csv", dtype=str)
        i_expiration = cc_df.loc[cc_df['number'] == self.number, 'expiration'].squeeze()
        i_cvc = cc_df.loc[cc_df['number'] == self.number, 'cvc'].squeeze()
        i_holder = cc_df.loc[cc_df['number'] == self.number, 'holder'].squeeze()

        if i_expiration == expiration and i_cvc == cvc and i_holder == holder:
            return True
        else:
            return False

hotel_id = int(input("Enter the id of the hotel: "))
hotel = Hotel(hotel_id)

if hotel.available() is True:
    credit_card = CreditCard("1234")
    if credit_card.validate("12/26", "123", "JOHN SMITH"):
        print("Successfully validated")
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        print(reservation_ticket.generate())
    else:
        print("There is a problem with your payment")
else:
    print("Hotel is not available")