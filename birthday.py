"""
birthday.py
Author: Johannes Testorf
Credit: none
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name = input("Hello, what is your name? ")
month = input("Hi " +name+", what was the name of the month you were born in? ")
year = input( "And what year were you born in, "+name+"? ")
day = input("And the day? ")

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

if month=="January":
    monthnum=1
else:
    if month=="February":
        monthnum=2
    else:
        if month=="March":
            monthnum=3
        else:
            if month=="April":
                monthnum=4
            else:
                if month=="May":
                    monthnum=5
                else:
                    if month=="June":
                        monthnum=6
                    else:
                        if month=="July":
                            monthnum=7
                        else:
                            if month=="August":
                                monthnum=8
                            else:
                                if month=="September":
                                    monthnum=9
                                else:
                                    if month=="October":
                                        monthnum=10
                                    else:
                                        if month=="November":
                                            monthnum=11
                                        else:
                                            if month=="December":
                                                monthnum=12
                                            
if int(year) in [1980, 1981, 1982, 1983, 1984,1985, 1986, 1987, 1988, 1989]:
    gen = "eighties"
else:
    if int(year) in [1990, 1991, 1992, 1993, 1994,1995, 1996, 1997, 1998, 1999]:
        gen = "nineties"
    else:
        if int(year) >= 2000:
            gen = "two thousands"
        else: 
            gen = "stone age"
if month in ["December", "January" "February:"]:
    season = "winter"
else:
        if month in ["March", "April", "May"]:
            season = "spring"
        else:
            if month in ["June", "July", "August"]:
                season = "summer"
            else:
                if month in ["September", "October", "November"]:
                 season = "fall"
                     
if month == "October" and int(day) == 31:
    print("You were born on Halloween!")
else:
    if todaymonth == int(monthnum) and int(day) == int(todaydate):
        print("Happy birthday!")
    else:
     print(name+", you are a "+season+" baby of the "+gen+".")