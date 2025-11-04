# Random module import kiya hai - isse computer random choices le payega
import random

'''
Game ke values ka meaning:
1 for snake (sanp)
-1 for water (paani) 
0 for gun (bandook)

Game Rules (Khel ke Niyam):
- Snake (1) water (-1) ko pee jata hai → Snake jeeta
- Water (-1) gun (0) ko rust karta hai → Water jeeta  
- Gun (0) snake (1) ko mar deti hai → Gun jeeti
'''

# Computer apni choice randomly select karta hai [-1, 0, 1] mein se
computer = random.choice([-1, 0, 1])

# User se input lete hai aur .lower() se lowercase mein convert karte hai
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Dictionary banaya hai user ke letter input ko number mein convert karne ke liye
youDict = {"s": 1, "w": -1, "g": 0}

# Reverse dictionary banaya hai numbers ko words mein convert karne ke liye
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check karte hai ki user ka input valid hai ya nahi
if youstr in youDict:
    # Agar input valid hai toh user ke choice ko number mein convert karte hai
    you = youDict[youstr]
    
    # Ab humare paas 2 numbers hai: you (user choice) aur computer (computer choice)
    # F-string use karke dono choices display karte hai
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
    
    # Pehla condition: agar dono ki choice same hai toh draw
    if computer == you:
        print("Its a draw")
    
    # Agar choices different hai toh game logic check karte hai
    else:
        # Condition 1: Computer = Water(-1) vs User = Snake(1) → User jeeta
        if computer == -1 and you == 1: 
            print("You win!")
        
        # Condition 2: Computer = Water(-1) vs User = Gun(0) → User hara
        elif computer == -1 and you == 0:
            print("You Lose!")
        
        # Condition 3: Computer = Snake(1) vs User = Water(-1) → User hara
        elif computer == 1 and you == -1:
            print("You lose!")
        
        # Condition 4: Computer = Snake(1) vs User = Gun(0) → User jeeta
        elif computer == 1 and you == 0:
            print("You Win!")
        
        # Condition 5: Computer = Gun(0) vs User = Water(-1) → User jeeta
        elif computer == 0 and you == -1:
            print("You Win!")
        
        # Condition 6: Computer = Gun(0) vs User = Snake(1) → User hara
        elif computer == 0 and you == 1:
            print("You Lose!")
        
        # Safety net: agar koi condition miss ho gayi toh error message
        else:
            print("Something went wrong!")

# Agar user ne invalid input diya hai (s, w, g ke alawa kuch aur)
else:
    print("Invalid input! Please enter 's' for snake, 'w' for water, or 'g' for gun")