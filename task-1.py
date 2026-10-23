


while True:
    speci = "!@#$%&*()_+?"
    upper=0
    lower=0
    digit=0
    special=0
    space=0
    print("="*30)
    user = input("ENter the password strongly more than 8: ")
    if user =="":
        print("Plz enter something")
    l = len(user)
    
    if(l>=8):
        for i in user:
            if i.isdigit() == True:
                digit+=1
            if i.islower() == True:
                lower+=1
            if i.isupper() == True:
                upper+=1
            if i ==' ':
                    space+=1
            for sp in speci:
                if sp == i:
                    special+=1
                
        if space>=1:
            print("Plz do not enter the space in the password")
        
        elif space ==0 and upper>=1 and lower>=1 and special>=1 and digit>=1:
            print("Your password is good to set !!")
            break
            
        elif space>=1:
            print("Plz do not enter the space in the password")
        elif upper==0:
            print("Plz Enter atleat one cap letter")
        elif lower==0:
            print("Plz Enter atleat one Lower letter")
        elif special==0:
            print("Plz Enter atleat one special letter")
        elif digit==0:
            print("Plz Enter atleat one Number")
    elif(l<8):
        print("Plz Enter the pasword with atleat 8 characters")
        
    elif(l>20):
        print("plz Enter the Password only in range of 8 to 20 only")
        
            

            
            
    
        
