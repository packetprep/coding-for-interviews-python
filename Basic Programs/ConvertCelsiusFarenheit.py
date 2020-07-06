"""
    # Program to convert Celsius to Farenheit
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""

# Read the temperature from user input
celsius = float(input("Enter the temperature in celsius: "))

# Conversion Logic
farenheit = (celsius * 1.8) + 32
result = round(farenheit, 2)

# print the result
print(result)
