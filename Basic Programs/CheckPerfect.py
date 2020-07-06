"""
    # Program to check if the given number is perfect
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""
"""
    Perfect - a positive integer that is equal to the sum of its proper divisors.

    For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6,
    so 6 is a perfect number

    eg: 6, 28, 496, 8128
"""


def perfect(num):
    """The perfect() will check if given argument is perfect number then
    returns 1 else 0 """
    divisorSum = 0
    for i in range(1,num):
        if num % i == 0:
            divisorSum = divisorSum + i
    if divisorSum == num:
        return 1
    else:
        return 0


# Take input from user
num = int(input("Enter the number:"))

# Check for Perfect
if perfect(num):
    print("Perfect Number")
else:
    print("it is not a Perfect Number")