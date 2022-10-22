annualIncome = float(input("Enter the Annual Income: "))
if annualIncome <= 250000:
    print("No TAX")
elif annualIncome <= 500000:
    incomeTaxAmount = annualIncome * 5/100
    print("Income TAX Amount: " + str(incomeTaxAmount))
elif annualIncome <= 1000000:
    incomeTaxAmount = annualIncome * 20/100
    print("Income TAX Amount: " + str(incomeTaxAmount))
elif annualIncome <= 5000000:
    incomeTaxAmount = annualIncome * 30 / 100
    print("Income TAX Amount: " + str(incomeTaxAmount))

