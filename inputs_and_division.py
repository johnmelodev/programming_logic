# Example of how you use inputs and division to calculate the hourly wage based on the monthly salary and hours worked per month.

monthly_salary = input('What is your monthly salary')
hours_worked_per_month = input('How many hours worked per month')
hourly_rate = int(monthly_salary) / int(hours_worked_per_month)
print(hourly_rate)
