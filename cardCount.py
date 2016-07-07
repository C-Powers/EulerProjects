def cc(card, count):
   if (card == 2 or card == 3 or card == 4 or card == 5 or card == 6):
       count = count + 1
   elif (card == 7 or card == 8 or card == 9):
       count = count + 0
   elif (card == 10 or card == 'J' or card == 'Q' or card == 'K'or card == 'A'):
       count = count -1
   if (count >0):
       print count, " Bet"
       return count
   elif (count <=0):
       print count, " Hold"
       return count



count = 0

count = cc('K', count)
