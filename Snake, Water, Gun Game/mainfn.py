# random module import kiya hai taki computer random choice le sake
import random

# Yeh function snake, water, gun game khelne ke liye hai
def snake_water_gun_game():
    '''
    Game ke rules:
    1 for snake (sanp)
    -1 for water (paani)
    0 for gun (bandook)
    
    Game logic:
    - Snake water ko pee jata hai (win)
    - Water gun ko rust karta hai (win) 
    - Gun snake ko mar deti hai (win)
    '''
    
    # Computer random choice leta hai -1, 0, ya 1 mein se
    computer = random.choice([-1, 0, 1])
    
    # User se input lete hai (s, w, ya g)
    youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    
    # Dictionary banaya hai user ke input ko number mein convert karne ke liye
    youDict = {"s": 1, "w": -1, "g": 0}
    
    # Reverse dictionary banaya hai numbers ko words mein convert karne ke liye display mein
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    # Check karte hai ki user ne sahi input diya hai ya nahi
    if youstr in youDict:
        # Agar sahi input hai toh user ke choice ko number mein convert karte hai
        you = youDict[youstr]
        
        # Ab humare paas 2 numbers hai - user ka choice aur computer ka choice
        # Dono choices ko words mein display karte hai
        print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
        
        # Pehla condition: agar dono ki choice same hai toh draw
        if computer == you:
            print("Its a draw")
        
        # Agar choices same nahi hai toh game ka logic check karte hai
        else:
            # Computer: Water (-1) vs User: Snake (1) -> User jeeta
            if computer == -1 and you == 1: 
                print("You win!")
            
            # Computer: Water (-1) vs User: Gun (0) -> User haara
            elif computer == -1 and you == 0:
                print("You Lose!")
            
            # Computer: Snake (1) vs User: Water (-1) -> User haara
            elif computer == 1 and you == -1:
                print("You lose!")
            
            # Computer: Snake (1) vs User: Gun (0) -> User jeeta
            elif computer == 1 and you == 0:
                print("You Win!")
            
            # Computer: Gun (0) vs User: Water (-1) -> User jeeta
            elif computer == 0 and you == -1:
                print("You Win!")
            
            # Computer: Gun (0) vs User: Snake (1) -> User haara
            elif computer == 0 and you == 1:
                print("You Lose!")
            
            # Safety check: agar koi condition miss ho gayi toh
            else:
                print("Something went wrong!")
    
    # Agar user ne galat input diya hai (s, w, g ke alawa kuch aur)
    else:
        print("Invalid input! Please enter 's' for snake, 'w' for water, or 'g' for gun")

# Game ko multiple times call karte hai (8 baar)
# Har baar naya game start hoga
snake_water_gun_game()  # Pehla game
snake_water_gun_game()  # Dusra game
snake_water_gun_game()  # Teesra game
snake_water_gun_game()  # Chautha game
snake_water_gun_game()  # Panchva game
