"""
    # Program to check if the given number is Armstrong
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""
"""
    A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.

    For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

"""


def armstrong(num):
    """The armstrong() will check if given argument is armstrong number then
    returns 1 else 0 """
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    if sum == num:
        return 1
    else:
        return 0


# Take input from user
num = int(input("Enter the number:"))

# Check for Armstrong
if armstrong(num):
    print("Armstrong Number")
else:
    print("it is not an Armstrong Number")