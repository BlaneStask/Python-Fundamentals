'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
user_input = int(input("Gimme the investment amount: "))
amount = int(user_input)
user_input2 = int(input("Gimme the interest rate as a percent: "))
rate = int(user_input2)
user_input3 = int(input("Gimme the number of years to invest: "))
years = int(user_input3)
user_input4 = int(input("Gimme the number of compounding periods: "))
periods = int(user_input4)

one_year = amount * ((1 + rate) ** periods)
future_value = years * one_year

print(future_value, "is the future value of your investment")