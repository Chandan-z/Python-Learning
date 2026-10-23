print("_________________ZERO SUS BANK OF MATRIX_____________")
print("="*55)
name = input("Enter your Name:")
print("User Plz Select the Option as 1 | 2 | 3 | 4 only")
print("="*55)
print("""1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Exit""")
print("="*55)
bank = 5000
while True:
    try :
        user = int(input("ENter the Number for the option :"))
    except:
        print("plz enter the number only")
    

        
    if user == 1:
        print(f"{name}'s Current Bank Balance is:$",bank)
        print("="*55)
    elif user == 2:
        while True:
            try:
                depo = int(input("Enter the Ammount to Deposite:"))
                bank+=depo
                break
            except:
                print("Plz enter the Ammount to Deposite in Number only")
        print(f"${depo} is Deposited to your account")
        print(f"{name}'s Balace after deposition ${bank}")
        print("="*55)
    elif user == 3:
        while True:
            try:
                withdraw = int(input("Enter the Ammount to Withdraw:"))
                bank-=withdraw
                break
            except:
                print("Plz enter the Ammount to Withdraw in Number only")
        print(f"${withdraw} is Withdrawn from your account")
        print(f"{name}'s Balace after WithDrwa is  ${bank}")
        print("="*55)
    
    elif user ==4:
        print(f"Bye {name} ")
        break
    else:
        print("Plz Select the Option as 1 | 2 | 3 | 4 only")
        print("="*55)

            
        
