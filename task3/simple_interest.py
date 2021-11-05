'''
This program is written to calculate the simple
interest of money
'''
principal = p = int(input("Please enter the value of principal:  "))
rate = r = int(input("Please enter the rate: "))
time = t = int(input("Please enter the time period here: "))

simple_interest = (p * r * t) / 100
#For better context
print(f"The simple interest is: {simple_interest}")
print(type(simple_interest))
