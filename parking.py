# Your parking gargage class should have the following methods:

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary





class parking_lot():
    def __init__(self): 
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.current_ticket = {}

    def take_ticket(self):
        if not self.parking_spaces:
            print("Parking lot is full.")
        ticket = self.tickets.pop(0)
        space = self.parking_spaces.pop(0)
        self.current_ticket[ticket]="unpaid" 
        print(self.tickets, self.parking_spaces, self.current_ticket)
        

    def pay_for_parking(self):
        ticket = int(input("What is your ticket no:"))

        if self.current_ticket[ticket] == "paid":
            print("Your ticket has been paid and you have 15mins to leave the parking lot.")
        
        else:
            print("Please pay for the parking ticket.")
            pay = input("Please enter amount: paid")
            if pay.lower()=="paid":
                print("Your ticket has been paid and you have 15mins to leave the parking lot.")
                self.current_ticket[ticket]="paid"
                

            self.tickets.append(ticket)
            self.parking_spaces.append(ticket)
            print(self.tickets, self.parking_spaces, self.current_ticket)

    def leave_garage(self):
        ticket = int(input("What is your ticket no:"))

        if self.current_ticket[ticket] == "paid":
            print("Thank you, have a nice day!")
        else:
            print("Please pay for the parking ticket.")
            self.pay_for_parking()
        

class UI():
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def my_func(self):
        while True:
            ask = input("What would you like to do? You can type: take/ leave/ pay.")

            if ask.lower() == "take":
                self.parking_lot.take_ticket()
            elif ask.lower() == "pay":
                self.parking_lot.pay_for_parking()
            elif ask.lower() == "leave": 
                self.parking_lot.leave_garage()
            else:
                print("Thank you, have a nice day!")  

parking = UI(parking_lot())
parking.my_func()