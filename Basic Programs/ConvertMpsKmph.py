"""
    # Program to convert Mps to Kmph
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""

# Read the input from user
mps = float(input("Enter the speed in mps: "))

# Conversion Logic
kmph = mps * 3.6
result = round(kmph,1)

# print the result
print(result)