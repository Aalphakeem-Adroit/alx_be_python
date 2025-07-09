monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")
monthly_savings = int(monthly_income) - int(monthly_expenses)

annual_interest = 5 / 100

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * int(annual_interest))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")