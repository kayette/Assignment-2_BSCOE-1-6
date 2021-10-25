applePrice=int(20)
orangePrice=int(25)
print("Hi there, welcome to our store! An apple costs 20 pesos, while an orange costs 25 pesos.")

appleAmount=int(input("How many apples do you want to purchase? "))
orangeAmount=int(input("How many oranges do you want to purchase? "))
appleTotal=applePrice*appleAmount
orangeTotal=orangePrice*orangeAmount

total=appleTotal+orangeTotal
print(f"The total amount is {total} pesos.")