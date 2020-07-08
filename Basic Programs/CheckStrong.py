"""
    # Program to check if the given number is perfect
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""
"""
    Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number.
    For example: 145 is an Strong number since 145 = 1! + 4! + 5!.
"""

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

def strong(num):
    """The strong() will check if given argument is strong number then
    returns 1 else 0 """
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + factorial(digit)
        temp = temp // 10
    if sum == num:
        return 1
    else:
        return 0


# Take input from user
num = int(input("Enter the number:"))

# Check for Strong
if strong(num):
    print("Strong Number")
else:
    print("it is not an Strong Number")