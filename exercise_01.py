"""
KPI Calculation:
The KPI Bonus is calculated as:
`1000 + salary * bonus percentage in decimal`
"""

BONUS = 1000

# 1) Ask the user to type his name

name_user = input("Enter your name: ")

# 2) Ask the user to type his salary value
# Convert his salary to a float

salary_value = input("Enter your salary value: ")

if "," in salary_value:
    salary_value = salary_value.replace(",", ".")
try:
    salary_value = float(salary_value)
except ValueError:
    print("Invalid salary value. Please, insert a valid number, like 1.0 or 1,0")


# 3) Ask the user to type his bonus value
# Convert his bonus to a float

bonus_percentage = input("Enter your bonus value: ")

if "," in bonus_percentage:
    bonus_percentage = bonus_percentage.replace(",", ".")

try:
    bonus_percentage = float(bonus_percentage)
except ValueError:
    print("Invalid value. Please, insert a valid numeber, like 0.10 or 0.20")


# 4) Calculate the final value bonus

final_salary_bonus = BONUS + (salary_value * bonus_percentage)


# 5) Print a message include the user name, salary and bonus

print(
    f"The user {name_user}, have a final salary with bonus value: {final_salary_bonus}"
)
