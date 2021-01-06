#Bank application

from firebase.firebase import FirebaseApplication
import random

def connectToFirebase():
    firebase = FirebaseApplication("https://bankoperations-5e273-default-rtdb.firebaseio.com/",None)
    return firebase

def createAccount():
    print("Welcome to New Account Creation")
    acno = random.randint(1000000000,9999999999)  #automatically generate account no
    print("Your Account No is "+str(acno))
    #acno = int(input("Enter Account No : "))
    firebase = connectToFirebase()
    acno_available = firebase.get("saving_accounts",acno)

    if acno_available:
        print("Account No is already Available")
    else:
        name = input("Enter Name : ")
        pin = int(input("Enter Pin no : "))
        o_balance = int(input("Enter Balance amount : "))
        data = {"name":name,"pin_no":pin,"balance":o_balance}
        firebase.put("saving_accounts",acno,data)
        print("New Account is Created")

def deposit():
    acno = int(input("Enter Account No : "))
    firebase = connectToFirebase()
    acno_available = firebase.get("saving_accounts", acno)
    if acno_available:
        deposit = int(input("Enter Amount to deposit : "))
        total_bal = acno_available["balance"]+deposit
        firebase.patch("saving_accounts/"+str(acno),{"balance":total_bal})
        print("Amount is deposited")
    else:
        print("Account No is Not Available")


def withdraw():
    acno = int(input("Enter Account No : "))
    firebase = connectToFirebase()
    acno_available = firebase.get("saving_accounts", acno)
    if acno_available:
        pin = int(input("Enter Pin : "))
        pin_available = firebase.get("saving_accounts",{"pin_no":pin})
        if  acno_available["pin_no"] == pin:
            withdraw = int(input("Enter amount to withdraw : "))
            total_balance = acno_available["balance"]-withdraw
            firebase.patch("saving_accounts/"+str(acno),{"balance":total_balance})
            print("Successfully withdrawl")
    else:
        print("Account No is Not Available")

def checkBalance():
    acno = int(input("Enter Account No : "))
    firebase = connectToFirebase()
    acno_available = firebase.get("saving_accounts", acno)
    if acno_available:
        print("Your Balance is :",acno_available["balance"])
        print("Thank you for using PC Bank")
    else:
        print("Account No is Not Available")

print("Welcome to PC Bank")
print("1)Create New Account")
print("2)Deposit")
print("3)Withdraw")
print("4)Check Balance")
option = int(input("Choose 1 Option :"))
if option == 1:
    createAccount()
elif option == 2:
    deposit()
elif option == 3:
    withdraw()
elif option == 4:
    checkBalance()
else:
    print("Select the option fron given menu")
    print("Thanks")