print("CALCULATE YOUR INCOME TAX")
name=input("enter your name:\n").upper()
total_amount=int(input("enter your gross annual income:\n$"))
dependants=int(input("total dependents:\n"))
standard_deduction=10000
taxable_amount=(total_amount-standard_deduction-(3000*dependants))
income_tax=0.2*taxable_amount
print(f"total income tax to be payed by {name} is {income_tax}" )