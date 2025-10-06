# Price of house is 1M
# if buyer has good credit,
# they need to put down 10%
# otherwise
# they need to put down 20%


buyer_goodcredit = False
house_price = 1000000

if buyer_goodcredit:
    payment = 0.1 * house_price
else:
    payment = 0.2 * house_price

print(f"So u need to pay: {payment}")
