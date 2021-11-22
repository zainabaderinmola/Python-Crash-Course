"""
Write a generic code that accepts a range of number from 
1 to 100, and check if a number in that range is divisible by 3, 
it should print 'FIZZ' and if it is divisible by 5, print 'BUZZ'
and if the number is divisible by both 3 and 5 print 'FIZZBUZZ'.
Goodluck!
e.g
[1, 2, 'Fizz', 4, 'Buzz'...]
==> 9 is divisible by 3
instead of the integer 9, it returns FIZZ
==> 10 is divisible by 5
instead of the integer 10, it returns BUZZ
==> 15 is divisible by both 5 and 3
instead of the integer 15, it returns FIZZBUZZ
"""

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZBUZZ")
    elif num% 3 == 0:
        print('FIZZ')
    elif num % 5 == 0:
        print("BUZZ")
    else:
        print(num)
        
