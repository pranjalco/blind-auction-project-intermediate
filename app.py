import art

"""
# Project 6: Blind Auction Project
### Description:
The Blind Auction Project allows users to participate in an auction where they can input their bids. The program 
collects user data (name and price) and stores it in a dictionary. It checks whether new bids need to be added and 
compares the bids to identify the highest one.

### Features:
- Collects user input for bids (name and price).
- Stores data in a dictionary ({name: price}).
- Uses while loops for repeated input and decision-making.
- Allows for bid comparisons to determine the highest bid.

# Level: Intermediate
Author: Pranjal Sarnaikpi
Date: 2024-12-03
"""

print(art.logo)
bidder_data = {}
winner_name = ""


def add_data_to_dict():
    """This function add data to dictionary based on input provided by user."""
    while True:
        name = input("What is your name: ")

        while True:
            bid = input("What is your bid: $")
            if bid.isdigit() and int(bid) > 0:
                break
            else:
                print("Please enter integer value grater than 0 for bid.")

        bidder_data[name] = bid
        any_bidders = input("Are there any other bidders present type (yes/no): ").lower()
        if any_bidders == "yes":
            print("\n" * 25)
            pass
        elif any_bidders == "no":
            break
        else:
            print("Error: Please enter 'yes' or 'no', quiting now")
            exit()


add_data_to_dict()


def check_highest_bid():
    global winner_name
    highest_bid = 0
    for key in bidder_data:
        if int(bidder_data[key]) > highest_bid:
            highest_bid = int(bidder_data[key])
            winner_name = key
        elif int(bidder_data[key]) == highest_bid:
            print("This is tie, please play again.")
            exit()
        else:
            pass

    return winner_name, highest_bid


winners_name, highest_bid_winner = check_highest_bid()
print(f"The winner is '{winners_name}' with bid of ${highest_bid_winner}")
