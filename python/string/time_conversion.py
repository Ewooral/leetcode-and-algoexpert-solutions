""" 
Python program to convert time from 12 hour to 24 hour format
Difficulty Level : Easy
Last Updated : 02 May, 2018
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note : Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock. Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock.

Examples :

Input : 11:21:30 PM
Output : 23:21:30

Input : 12:12:20 AM
Output : 00:12:20

"""


def convert24(str1):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and  remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


# Driver Code
print(convert24("11:05:45 PM"))
