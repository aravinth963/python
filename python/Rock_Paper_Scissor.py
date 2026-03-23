import random 

#key => value
#"r" -> "🪨"
#"p" -> "📃"
#"s" -> "✂️"

emojis = {"r":"🪨","p":"📃", "s":"✂️"}
choices = ["r", "p", "s"]

while True:
    choice = input("Rock, Paper or Scissors?(r/p/s): ").lower()

    if choice not in choices:
        print("invalid choice") 
        continue

    computer_choice =  random.choice(choices)

    print(f"you chose {emojis[choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if(choice == computer_choice):
        print("tie")
    elif(
         (choice == "r" and computer_choice == "s") or 
         (choice == "s" and computer_choice == "p") or 
         (choice == "p" and computer_choice == "r")):
        print("you win")
    else:
        print("lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == "n":
        break
