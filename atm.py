import random



class Atm:
    def __init__(self,name,account_num,pin,balance):
        self.name=name
        self.account_num=account_num
        self.pin=pin
        self.balance=balance

    def deposit(self,amount,in_pin):
        self.amount=amount
        self.in_pin = in_pin
        if self.in_pin == self.pin:
            if self.amount <25001:
                self.balance=self.balance + self.amount
                print("Amount was successfully deposit..")
                print("Remaining balance is : ",self.balance)
                print()
            else:
                print("Max deposit amount is 25000 per transaction!")
        else:
            print("incorrect pin!")
            print()

    def withdraw(self,amount,in_pin):
        self.in_pin = in_pin
        if self.in_pin == self.pin:
            self.amount=amount
            if self.amount > self.balance:
                print("Insufficient fund!")
                print()
            elif self.amount > 25000 :
                print("withdrawn amount is under 25000 per transaction!")
                print()
            else:
                self.balance=self.balance - self.amount
                print("Amount was successfully withdraw..")
                print("Remaining balance is : ",self.balance)
                print()
        else:
            print("incorrect pin!")
            print()
    
    def balance_enquiry(self,in_pin):
        self.in_pin=in_pin
        if self.in_pin == self.pin:
            print("Available balance is : ",self.balance)
            print()

        else:
            print("Incorrect pin!")
            print()

    def change_pin(self,new_pin,confirm_pin):
        self.new_pin = new_pin
        self.confirm_pin = confirm_pin
        if self.new_pin == self.pin:
            print("Pin is matched to previous pin!")
            print()

        elif self.new_pin == self.confirm_pin:
            self.pin = self.new_pin
            print("Pin was successfully changed")
            print()
            
        else:
            print("Enter wrong pin!")
            print()

    def choices(self):

        print("""
              menu:
              1.deposit
              2.withdraw
              3.balance enquiry
              4.change pin
              5.quit
              """)
        
        while True:

            self.option=int(input("Enter the value: "))
            if self.option not in range(1,5+1):
                print("Enter the values between 1 to 5 only:")
            else:
                if self.option == 1:
                    amount = int(input("How much you want to deposit:"))
                    in_pin = int(input("Enter pin : "))
                
                    atm.deposit(amount,in_pin)
                elif self.option == 2:
                    amount = int(input("How much you want to withdraw:"))
                    in_pin = int(input("Enter pin : "))
                    atm.withdraw(amount,in_pin)
                elif self.option == 3:
                    in_pin = int(input("Enter pin : "))
                    atm.balance_enquiry(in_pin)
                elif self.option == 4:
                    new_pin = int(input("Enter new pin : "))
                    confirm_pin = int(input("Enter confirm pin : "))
                    atm.change_pin(new_pin,confirm_pin)
                elif self.option == 5:
                    print(f"""
                        printing receipt..........
                        ******************************************
                        Transaction is now complete.                         
                        Transaction number: {random.randint(10000, 1000000)} 
                        Account holder: {self.name.upper()}                  
                        Account number: {self.account_num}*****                
                        Available balance: {self.balance}                    
 
                        Thanks for choosing us as your bank                  
                        ******************************************
                        """)
                    break

print("-------------- WELCOME TO MY BANK ---------------")
name=input("Enter your name : ")
account_num=int(input("Enter your account number : "))
pin=int(input("enter pin : "))
balance=float(input("enter deposit amount : "))
print("Account created successfully...")
atm=Atm(name,account_num,pin,balance)
atm.choices()
# while True:
#     input = input("Do you want to do any transaction?(y/z):").lower()
#     if input == "y":
#         atm.choices()
#     elif input == "n":
#         print("""
#             Thanks for choosing MY BANK 
#             Visit us again!
#               """)
#         break
#     else:
#         print("Wrong input!")

            




    



