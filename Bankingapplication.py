class Bank:
    Branch_name      = 'Marathahlli'
    Rate_of_interest = 0.7
    Bank_name        = 'SBI'
    def __init__(self, name, phone, pin, balance):
        self.Name    =  name
        self.Phone   =  phone
        self.Pin     =  pin
        self.Balance =  balance
    def deposit(self):
        amt = int(input("Enter the amount...  "))
        self.Balance += amt
        print("Successfully credited...")
    def check(self):
        if self.Pin == int(input("Enter your pin")):
            return True
        return False
    def balance(self):
        if self.check():
            print("Your balance is {}".format(self.Balance))
        else:
            print("Please enter a correct pin")
    def withdrawl(self):
        amt = int(input("Enter the amount.."))
        if self.check():
            if amt <= self.Balance:
                self.Balance -= amt
                print("{} is credited successfully".format(amt))
            else:
                print("Insufficient amount")
        else:
             print("Please enter a correct pin")
    def changepin(self):
        if self.check():
            self.Pin = int(input("Eneter your new pin"))
            print("Pin updated successfully")
        else:
            print("Please enter a correct pin")
user1 = Bank('Abhishek', 8592915183, 123, 2000)
user2 = Bank('Abhi', 8592915184, 124, 2000)
user1.deposit()
user1.balance()
user1.withdrawl()
user1.balance()
                
            
