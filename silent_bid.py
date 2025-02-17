
bidders = {}

name = input("enter your name : ")
bid = int(input("enter your bid $"))
bidders[name] = bid

while True:
    check_continue = input("are there other bidders? 'y' or 'n' ")
    if check_continue == "y":
        print("\n" * 100)
        name = input("enter your name : ")
        bid = int(input("enter your bid $"))
        bidders[name] = bid
    elif check_continue == "n":
        break
max_bid = 0
winner = max(bidders, key=bidders.get)
print(f"the winner is {winner} ")