"""
    # Program to calculate the factorial of given number
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""

# Read the input from user
num = int(input("Enter the number: "))

factorial = 1
for i in range(1,num+1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")



