class Atm:
    def __init__(self,cardnumber,pin):
        self.cardNumber = cardnumber
        self.pin = pin
    def check_balence(self):
        print("Your balence is 50,000")

def main():
    cardNumber=input("Enter card number:")
    pin=input("Enter pin:")

main()