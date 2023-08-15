investment=100
i = 0
while (investment<=1000):
    gain=investment*0.1
    investment = investment+gain
    if investment >= 1000:
        print(i)
        print(investment)
    i = i+1
   

# Reusable code

initial_investment=int(input("How much is the inital investment?"))
target_value= float(input("How much would you like to make?"))
interest_rate= float(input("What is the interest rate being offered?"))
i = 0
while (initial_investment<=target_value):
    gain=investment*interest_rate
    initial_investment = initial_investment+gain
    if initial_investment >= target_value:
        print(i)
        print(initial_investment)
    i = i+1
