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

class SpaHotel(Hotel):
    pass

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

class SpaReservationTicket(ReservationTicket):
    def generate(self):
        content = f"""
        Thank you for your SPA reservation
        Here are your SPA booking data:
        Name: {self.name}
        Hotel: {self.hotel.get_name()}"""

        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvc, holder):
        cc_df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
        cc_data = {"number": self.number, "expiration": expiration, "cvc": cvc, "holder": holder}

        if cc_data in cc_df:
            return True
        else:
            return False

        # An alternative solution I earlier made
        # i_expiration = cc_df.loc[cc_df['number'] == self.number, 'expiration'].squeeze()
        # i_cvc = cc_df.loc[cc_df['number'] == self.number, 'cvc'].squeeze()
        # i_holder = cc_df.loc[cc_df['number'] == self.number, 'holder'].squeeze()
        # if i_expiration == expiration and i_cvc == cvc and i_holder == holder:
        #     return True
        # else:
        #     return False

class SecureCreditCard(CreditCard):
    def authenticate(self, input_password):
        cc_security_df = pd.read_csv("card-security.csv", dtype=str)
        password = cc_security_df.loc[cc_security_df['number'] == self.number, 'password'].squeeze()

        if input_password == password:
            return True
        else:
            return False

print(hotel_df)
hotel_id = int(input("Enter the id of the hotel: "))
hotel = Hotel(hotel_id)

if hotel.available() is True:
    credit_card = SecureCreditCard("1234")
    if credit_card.validate("12/26", "123", "JOHN SMITH"):
        if credit_card.authenticate("mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
            spa_invitation = input("Do you want to book a spa package?")

            if spa_invitation == "yes":
                spa_reservation_ticket = SpaReservationTicket(reservation_ticket)
                print(spa_reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There is a problem with your payment")
else:
    print("Hotel is not available")