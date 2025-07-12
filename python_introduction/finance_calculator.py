monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_income = float(monthly_income)
monthly_expenses = float(monthly_expenses) 

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings assuming a simple annual interest rate of 5%
annual_savings = monthly_savings * 12 + (monthly_savings * 0.05)

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}")
print(f"Your projected annual savings with a 5% interest rate is: ${annual_savings:.2f}")