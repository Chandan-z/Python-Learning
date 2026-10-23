print("This is Short AI")
print("-----------------------")
while True:
    user = input("Chat with me bro:")
    length = len(user)
    o=()
    hh=()
    
    for i in range(length):
        
        h = user[i]# captures very index in loop
        if (h=="h") or(h=="H"):
            
            hh=(i)# captures index in loop for h
    for ii in range(length):
        
        o = user[ii]# captures very index in loop
        if (o=="i") or(o=="I"):
            
            oo=(ii+1)# captures index in loop for i

        
    #print(hh)# h index  possition 
    #print(oo)# i index possition
    if (user[hh:oo]==("hi")) or (user[hh:oo]==("Hi")) or (user[hh:oo]==("HI")):
        print("hi bro  ")
            
           
  
                
                
            
    
    
        
            
            
            
    break
