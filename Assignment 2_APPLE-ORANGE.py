applePrice=int(20)
orangePrice=int(25)
print("\nHi there, welcome to our store! An apple costs 20 pesos, while an orange costs 25 pesos. \n ")

appleAmount=int(input("How many apples do you want to purchase? "))
orangeAmount=int(input("How many oranges do you want to purchase? "))
appleTotal=applePrice*appleAmount
orangeTotal=orangePrice*orangeAmount

total=appleTotal+orangeTotal
print(f"\nThe total amount is {total} pesos. \n")