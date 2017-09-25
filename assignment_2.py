'''
with using data No_of_shares, Purchase_Price, Current_Value data, running this code will generate following

STOCK                        SHARE#                              EARNINGS/LOSS

--------------------------------------------------------------------------------------------------

GOOGL                            125                                           $21026.25

MSFT                                 85                                           $1397.4

RDS-A                              400                                           $2464

AIG                                   235                                          $3599.1

FB                                    150                                            $7221

'''


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
    print ('{}       {}       ${}'.format(Stock_Symbols[i], No_of_shares[i],round(GAIN_or_LOSS[i])))

    
    
