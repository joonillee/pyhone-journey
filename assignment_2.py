#ICT4370 Week 2 Assignment 2 Joon Lee 9/24/2017

#reading data to lists
Stock_Symbols = ['GOOGL', 'MSFT ', 'RDS-A', 'AIG  ', 'FB   ']
No_of_shares = [125, 85, 400, 235, 150]
Purchase_Price = [772.88, 56.60, 49.58, 54.21, 124.31]
Current_Value = [941.53, 73.04, 55.74, 65.27, 172.45]




#calculating gain or loss and keeping it in a list
GAIN_or_LOSS = []

for i in range(len(Stock_Symbols)):
    GAIN_or_LOSS.append((Current_Value[i]-Purchase_Price[i])*No_of_shares[i])




#printing required data
print ("Stock ownership for Joon Lee")
print ("----------------------------------------")
print ("STOCK       SHARE#       EARNINGS/LOSS")
for i in range(len(Stock_Symbols)):
    print ('{}       {}       ${}'.format(Stock_Symbols[i], No_of_shares[i],GAIN_or_LOSS[i]))
