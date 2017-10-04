"""

Code creates a report,calculating how much the investor
has earned or lost.

step 1) Create the lists.
step 2) Print the header.
step 3) Iterate the list.
step 4) Calculating the earning.
step 4) Print the earning.
"""

# Stock information.
stock_symbol = ["GOOGL", "MSFT", "RDS-A", "AIG", "FB"]
shares = [125, 85, 400, 235, 150]
bought_price = [772.88,  56.60, 49.58, 54.21, 124.31]
current_price = [941.53, 73.04, 55.74, 65.27, 172.45]

# Print header.
print("Stock ownership for Bob Smith")
print("----------------------------------------")
print("stock \t Shares \t Earning")

# Method 1. This method uses a for loop and a counter.
counter = 0
for i in stock_symbol:
    # Get values from each list based on the index position.
    share = shares[counter]
    c_price = current_price[counter]
    b_price = bought_price[counter]
    # Calucate the persons earning/lose from the stock.
    # The forumla is Shares own * (current price - bought price)
    earning = share * (c_price - b_price)
    print(i, "\t", shares[counter], "\t", earning)
    counter += 1

# Method 2.
# Print header.
print("Stock ownership for Bob Smith")
print("----------------------------------------")
print("stock \t Shares \t Earning")
# Use enumerate to interate the list and get the index postion.
for i, val in enumerate(stock_symbol):
    # Calucate the persons earning/lose from the stock.
    # The forumla is Shares own * (current price - bought price)
    earning = shares[i] * (current_price[i] - bought_price[i])
    print(val, "\t", shares[i], "\t", earning)


# Method 3.
stock_info = [["Bob Smith", [["GOOGL", 125, 772.88, 941.53,],
                ["MSFT", 85, 56.60, 73.04],
                ["RDS-A", 400, 49.58, 55.74],
                ["AIG", 235, 54.21, 65.27],
                ["FB", 150, 124.31, 172.45]]],
                ["Steve Jobs", [["AAPL", 10000, 5.00, 150.00],
                ["VZ", 100, 50, 49]]
                ]]


# This method uses nested loops. This supports being able to have
# multiple people stock information.
# First loop to interate each header information including person name.
for i in stock_info:
    name = i[0]
    print("Stock ownership for {0}".format(name))
    print("----------------------------------------")
    print("stock \t Shares \t Earning")
    # Second loop to interate the stock information for each person.
    for j in i[1]:
        # Calucate the persons earning/lose from the stock.
        # The forumla is Shares own * (current price - bought price)
        earning = j[1] * (j[3] - j[2])
        print(j[0], "\t", j[1], "\t", earning)
