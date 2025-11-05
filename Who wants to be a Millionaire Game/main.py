import random

# ------------------ QUESTION BANK ------------------
# Format: question, dictionary of options, correct answer key

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
initial_prize = 10000
current_prize = initial_prize
total_won = 0

random.shuffle(questions)

print("🎮 Welcome to Who Wants To Be A Millionaire!")
input("Press ENTER to start...\n")

# ------------------ GAME LOOP ------------------
for q in questions:
    print(f"\n📂 Category: {q['category']}")
    print(f"❓ {q['question']}")

    # ✅ Shuffle options
    option_items = list(q["options"].items())  # convert dict to pair list
    random.shuffle(option_items)              # shuffle options

    # ✅ Map new labels A/B/C/D after shuffle
    new_labels = ["A","B","C","D"]
    shuffled_options = {}
    correct_label = ""

    for new_label, (old_label, text) in zip(new_labels, option_items):
        shuffled_options[new_label] = text
        if old_label == q["answer"]:         # match original correct answer
            correct_label = new_label        # assign new correct label

    # Display options
    for label, text in shuffled_options.items():
        print(f" {label}) {text}")

    # Get user answer
    user = input("\nYour answer (A/B/C/D): ").upper()

    # Check answer
    if user == correct_label:
        print("✅ Correct!")
        total_won += current_prize
        print(f"💰 Won: ₹{current_prize}")

        # Prize multiplier 1.5x – 2.5x
        multiplier = round(random.uniform(1.5, 2.5), 2)
        current_prize = int(current_prize * multiplier)
        print(f"⬆️ Next prize: ₹{current_prize}")
    else:
        print("❌ Wrong Answer! GAME OVER")
        print(f"✅ Correct Answer was → {correct_label}")
        break

print("\n🏁 GAME OVER")
print(f"🎉 Total Money Won: ₹{total_won}")
