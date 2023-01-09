fresh=int(input("enter the number of fresh loves purchased"))
old=int(input("enter the number of day old loves purchased"))
print("Regular price: Rs.185.00")
fresh_amount = 185.00*float(fresh)
old_amount = (185*0.4)*float(old)
Total=fresh_amount+old_amount
print("Amount of new loves:Rs " ,fresh_amount)
print("Amount of dy old loves: Rs" ,old_amount)
print("Total amount: Rs" ,Total)
