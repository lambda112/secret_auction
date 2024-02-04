from os import system

bidders = {}
print("Welcome to the secret auction!")


def bidding_func():
    
    while True:
        try:
            name = input("What is your name?: ").capitalize()
            bid = int(input (f"Hello {name}! What is your bid?: £"))
            bidders[name] = bid
            restart = input("Are there any other bidders! Yes or No?: ").lower()
            break
        except ValueError:
            print("Enter a number please!\n")


    return restart


while "yes" in bidding_func():
    system("cls")

print(bidders)
