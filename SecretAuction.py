from IPython import get_ipython

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print (logo)
print ("Welcome to the secret auction program!")

auction = {
    
    "Names" : [],
    "Bids" : [],
       
    }

def add_name (name):
    auction["Names"].append(name)
    
def add_bid (bid):
    auction["Bids"].append(bid)
    
answer = "yes"
highest_bid = 0
highest_bidder = ''
bid_amount = 0

while answer == "yes":
    
    name = input("Whats your name?: ")
    add_name(name)
    bid = int(input("Whats your bid?: $"))
    add_bid(bid)
    answer = input("Are there more bidders? Type 'yes' or 'no': ")
    get_ipython().magic('clear')

if answer == "no":
    for bid in range (len(auction["Bids"])):
            bid_amount = auction["Bids"][bid]
            
            if highest_bid < bid_amount:
                highest_bid = bid_amount
                highest_bidder = auction["Names"][bid]

print("The winner is " + highest_bidder + " with a bid of " + "$" + str(highest_bid) + "!!!")

