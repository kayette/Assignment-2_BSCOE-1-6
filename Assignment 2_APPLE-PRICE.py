myMoney=int(input("Enter the amount of money you have: "))
applePrice=int(input("Enter your desired price for one apple: "))
maxApple=int(myMoney/applePrice)
changeAmount=myMoney-maxApple*applePrice
neededAmount=applePrice-myMoney
if maxApple > 1: print(f"You can buy {maxApple} apples and your change is {changeAmount} pesos.")
if maxApple == 1: print(f"You can buy {maxApple} apple and your change is {changeAmount} pesos.")
if maxApple <= 0: print(f"You cannot buy any apples. You need {neededAmount} more pesos to complete a purchase.")