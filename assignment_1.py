# ICT4370 Assignment #1 Joon Lee
# My mentality here was to write simple code as possible, not sure if I achieved but here it is.
# I was able to ask users questions for desired answers to print once all questions are answered

a = input("Please enter your stock symbol: ")
b = input("How many Shares do you own currently?: ")
c = input("What was the original per share purchase price?: ")
d = input("what is current price per share?: ")

# I was having many errors and trouble getting result that can be printed.
# I was getting error on how str can not be multiplied
# so, I had to change the answers from above questions to int and float to make the line #19 work
x = int(b)
y = float(c)
z = float(d)

# then when try to print this using line #35, got error on how it must be string to display the result
# so had to change the price to str by using code on line #21
price = int((x*y)-(x*z))
price_1 = abs(price)
price_2 = str(price_1)

# One thing I couln't figure out here was that when there is loss, it displays the negative sign but
# when there is an earnings, I couldn't get rid of negative sign.. searched many places
# (maybe I am not good at searching for what I exactly need now) but just couldn't figure it out..
# you can deduct a point or more but when grading, but telling me how to do this would be greatly appreciated..

# UPDATE: I figured out, not sure this is the most efficient way but I was able to chnage - number from #19 to
# absolute number so that it can return postive number #20 to display whether the result is positive or negative number
# then change that number to string so that it displays correctly without errors on line #35

print (a + ": " + b + " Shares")
print ("Purchase Price: " + c)
print ("Current Price per Share: " + d)
print ("Earnings/Loss to-date: $" + price_2)

# Overall, this was not as simple as I originally thought but definately challenged me to think,try until it works
# not happy that I spent many hours on this but at least, learn few tricks along the way
