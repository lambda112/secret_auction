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


num = 0
for i in bidders:
    if num < bidders[i]:
        num = bidders[i]
        winner = i


system("cls")
print(f"The winners is {winner} with a bid of £{bidders[winner]}!")