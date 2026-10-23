import random

def choice():
    print("=========== Rock_Paper_Scissor =========")
    print("1. Rock \n2. Paper \n3. Scissor")

def computer():
    return random.randint(1,3)

def check_win(user,computer):
    if user == computer :
        return "tie"

    elif user == 1 and computer == 3 or user == 2 and computer ==1 or user == 3 and computer == 2:
        return "win"
    else:
        return "lose"

def table(user):
    if user == 1:
        print("Rock")
    elif user == 2:
        print("Paper")
    elif user == 3:
        print("Scissor")
    
def display_win(check_win,user,computer,you,bot):
    print("___________________________")
    print("You :",end="")
    table(user)
    print("Computer :",end="")
    table(computer)

    
    if check_win == "tie":
        print("Tie")
    elif(check_win == "win"):
        print("You Won !!!")
        you+=1
    elif check_win == "lose":
        print("Computer Won ;)")
        bot+=1
    print("___________________________")
    
    
    if check_win!= "tie":
        print("Score -")
        print(f"You :{you}")
        print(f"Computer :{bot}")
    print("============================")
    return you, bot
        
def final_score(you,bot):
    if you == 5:
        print("You Won this Match !!")
        print("Your score :",you)
        print("Computer score :",bot)                 
    elif bot ==5:
        print("You Lost this Match !!")
        print("Your score :",you)
        print("Computer score :",bot)
    print("============================")
    print()   

    
choice()
run = True

while run:
    you =0
    bot =0
    round_ = True
    while round_:
        while True:
            try:
                user = int(input("Enter the choise (1,2,3):"))
                if 1 <= user <= 3:
                    break
                else:
                    print("Plz select only (1,2,3)")
            except ValueError:
                print("Invalid Option !")
        comp = computer()
        checkwin = check_win(user,comp)
        you, bot = display_win(checkwin, user, comp, you, bot)
        
        if you ==5 or bot ==5:
            final_score(you,bot)
            round_ = False
            
            con =True
            while con:
                cont = input("Enter countinue or Q to quit :")
                if cont == "q" or cont == "Q":
                    run =False
                    con =False
                    break
                else:
                    con = False
                
