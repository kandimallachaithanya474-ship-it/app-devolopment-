import random

quotes = [
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt")
]

while True:
    print("\n1. Show Quote  2. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        q = random.choice(quotes)
        print("\nQuote:", q[0])
        print("Author:", q[1])
    elif choice == "2":
        break
    else:
        print("Invalid choice")