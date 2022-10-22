pricipalAmount = int(input("Enter the Pricipal Amount: "))
interestRate = float(input("Enter the Interest Rate: "))
years = float(input("Enter the number of years: "))
simpleInterest = (pricipalAmount * interestRate * years) / 100
print("Simple Interest: " + str(simpleInterest))
