print("Welcome to the secret auction!")

bidders = {}
name = input("What is your name?: ").capitalize()


while True:
    try:
        bid = int(input (f"Hello {name}! What is your bid?: £"))
        break
    except ValueError:
        print("Enter a number please!\n")


restart = input("Are there any other bidders! Yes or No?: ").lower()

print(name)
print(bid)
print(restart)