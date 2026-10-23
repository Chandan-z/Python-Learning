import json
data_base = "data_base.json"
with open(data_base,"r") as file:
    menu = json.load(file)

    
print("="*10,"ZERO SUS CART","="*10)

cart =[]
total=0

for key,value in menu.items():
    print(f"{key:20}- Rs.{value:.2f}")
print("="*30)
while True:
    user = input("Enter the food(q to quit):")
    if user =="q" or user=="Q":
        break
    elif menu.get(user) is not None:
        cart.append(user)
    else:
        print("Plz enter the correct food")
print("="*30)
print("="*30)
print("Your cart:")
for user in cart:
    total+=menu.get(user)
    print(user)
print("="*30)
print(f"your total is Rs.{total}/-")
print("="*30)
        
