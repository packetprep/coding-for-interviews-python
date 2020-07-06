"""
    # Program to check if the given number is prime
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""

# Prime - a number that is divisible only by itself and 1


def prime(num):
    """The prime() function checks if given argument is prime
    and return 1 else 0"""
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1


# Take input from user
number = int(input("Enter the number:"))

# Check for Palindrome
if prime(number):
    print("Prime")
else:
    print("Not prime")
