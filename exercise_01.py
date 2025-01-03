BONUS_CONSTANT = 1000

# 1) Ask the user to type his name

name_user = input('Enter your name: ')

# 2) Ask the user to type his salary value
# Convert his salary to a float

salary_value = float(input('Enter your salary value: '))


# 3) Ask the user to type his bonus value
# Convert his bonus to a float

bonus_value = float(input('Enter your bonus value: '))

# 4) Calculate the final value bonus

final_bonus = BONUS_CONSTANT + salary_value + bonus_value


# 5) Print a message include the user name, salary and bonus

print(f'The user {name_user}, have a final bonus value: {final_bonus}')
