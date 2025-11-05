# Importing random module to use functions for randomness (like random value, shuffle etc.)
import random

# ------------------ QUESTION BANK ------------------
# Each question is stored as a dictionary for structured data storage.
# Format: category, question text, options (dict), correct answer key (A/B/C/D)
questions = [
    {"category":"Indian Constitution (Easy)",
     "question":"Which article deals with Right to Equality?",
     "options":{"A":"Article 14","B":"Article 19","C":"Article 21","D":"Article 32"},
     "answer":"A"},

    {"category":"Indian Constitution (Easy)",
     "question":"Who is the Father of Indian Constitution?",
     "options":{"A":"Mahatma Gandhi","B":"B. R. Ambedkar","C":"Nehru","D":"Sardar Patel"},
     "answer":"B"},

    {"category":"Polity (Hard)",
     "question":"Anti-Defection law is in which Schedule?",
     "options":{"A":"7th","B":"8th","C":"10th","D":"11th"},
     "answer":"C"},

    {"category":"Polity (Hard)",
     "question":"Who appoints the Chief Election Commissioner?",
     "options":{"A":"Prime Minister","B":"President","C":"Lok Sabha","D":"CJI"},
     "answer":"B"},

    {"category":"General Knowledge",
     "question":"Longest river in the world?",
     "options":{"A":"Amazon","B":"Ganga","C":"Nile","D":"Yangtze"},
     "answer":"C"},

    {"category":"General Knowledge",
     "question":"Largest animal?",
     "options":{"A":"Elephant","B":"Blue Whale","C":"Giraffe","D":"Shark"},
     "answer":"B"},

    {"category":"Cinema",
     "question":"First Oscar for India?",
     "options":{"A":"Lagaan","B":"RRR","C":"The Elephant Whisperers","D":"Slumdog Millionaire"},
     "answer":"C"},

    {"category":"Cinema",
     "question":"Father of Indian Cinema?",
     "options":{"A":"Guru Dutt","B":"Ray","C":"Phalke","D":"Yash Chopra"},
     "answer":"C"},

    {"category":"History",
     "question":"Year of 1857 revolt?",
     "options":{"A":"1857","B":"1848","C":"1850","D":"1862"},
     "answer":"A"},

    {"category":"History",
     "question":"Founder of Maurya Empire?",
     "options":{"A":"Ashoka","B":"Chandragupta Maurya","C":"Bindusara","D":"Chanakya"},
     "answer":"B"},

    {"category":"History",
     "question":"First Mughal Emperor?",
     "options":{"A":"Humayun","B":"Akbar","C":"Babur","D":"Jahangir"},
     "answer":"C"},
]

# ------------------ GAME SETTINGS ------------------
initial_prize = 10000  # Starting money per question
current_prize = initial_prize  # Current prize changes after each correct answer
total_won = 0  # To accumulate total winnings

# Shuffle the question order so game is different every time
random.shuffle(questions)

print("🎮 Welcome to Who Wants To Be A Millionaire!")
input("Press ENTER to start...\n")  # Pauses until user presses Enter

# ------------------ GAME LOOP ------------------
# Loop through every dictionary in questions list one by one
for q in questions:
    
    print(f"\n📂 Category: {q['category']}")        # Display question category
    print(f"❓ {q['question']}")                    # Display actual question text

    # ✅ Shuffle answer options so they appear randomly every time

    option_items = list(q["options"].items())       # Convert dict to list of key-value pairs e.g. [("A","Amazon"), ...]
    random.shuffle(option_items)                    # Shuffle pairs so options change position

    # New option labels after shuffle
    new_labels = ["A","B","C","D"]

    shuffled_options = {}  # New dict for shuffled answers
    correct_label = ""     # To store which new label is correct answer

    # Assign new label to shuffled options
    for new_label, (old_label, text) in zip(new_labels, option_items):
        shuffled_options[new_label] = text    # Create new option dictionary
        
        # If the shuffled option was previously correct, we update correct answer label
        if old_label == q["answer"]:
            correct_label = new_label         # Save new correct answer key

    # Display shuffled options
    for label, text in shuffled_options.items():
        print(f" {label}) {text}")

    # Get answer from user & convert to uppercase so "a" or "A" both work
    user = input("\nYour answer (A/B/C/D): ").upper()

    # Check if answer is correct
    if user == correct_label:
        print("✅ Correct!")
        
        # Add current prize to total won
        total_won += current_prize
        print(f"💰 You Won: ₹{current_prize}")

        # Increase prize by random multiplier between 1.5 to 2.5
        multiplier = round(random.uniform(1.5, 2.5), 2)
        current_prize = int(current_prize * multiplier) # Increase prize for next question
        print(f"⬆️ Next Prize: ₹{current_prize}")

    else:
        print("❌ Wrong Answer! GAME OVER")
        print(f"✅ Correct Answer was → {correct_label}")
        break  # End game on wrong answer

# ------------------ END GAME ------------------
print("\n🏁 GAME OVER")
print(f"🎉 Total Money Won: ₹{total_won}")
