#Bank operation using OOP
class Bank:
    bankname="SBI"
    address="14/4 vikas nagar,neemuch"
    #create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0 #set account balance to 0.0
        print(f'Hello {self.username} congrats! your account created successfully')
    #deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited successfully')
    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully.')
        else:
            print("Insufficent Fund....")
    #Ministatement
    def ministatement(self):
        print(f'Your account Balance is {self.balance}')
print(f'welcome to {Bank.bankname}')
username=input("Enter your name:-")
pan=input("Enter Pan Card number:-") 
address=input("Enter Your address:-")
b=Bank(username,pan,address)  #object creation based on user provided data
while True:
    print('\n Please Select any option:- ')
    print('1.Deposit \n 2.Withdraw \n 3.Ministatement \n 4.Stop')
    option=int(input(" "))  
    if option==1:
        amount=float(input('Enter Deposited Amount:-'))
        b.deposit(amount)
    elif option==2:
        amount=float(input("Enter withdraw amount:-"))
        b.withdraw(amount)
    elif option==3:
        b.ministatement()
    elif option==4:
        print("Thanks for using SBI.......")
        break
    else:
        print("Invalid option plz select a valid option")        
          
