from art import logo
#HINT: You can call clear() to clear the output in the console
print(logo)

bids = {}
more_bids = True


def find_highest_bidder(all_bids):
    highest = 0
    winner = ''
    # for loop in dictionary loops through KEYS not values
    for bidder in all_bids:
        # print(f'bidder is {bidder}')
        amount = all_bids[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")


while more_bids == True:
    name = input('Enter your name\n')
    price = int(input('Place your bid \n$'))
    bids[name] = price

    bidding = input('Are there more bids? (yes or no)\n')
    if bidding == 'no':
        more_bids = False
        find_highest_bidder(bids)