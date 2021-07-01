# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:24:12 2021

@author: troya
"""

import regex as re


Dates = 'People like to write their dates in different formats like these 08/23/2021, 103021, February 12, 2021'

print(Dates)
print()
String1 = re.sub(r'(\d{2})(\d{2})(\d{2})', r'\1/\2/20\3', Dates, count=0, flags=0)
print("mmddyy converted to mm/dd/yyyy: ")
print(String1)
print()

# A start down the path to converting using regex:

Dates1 = re.sub('January','01',Dates)
Dates2 = re.sub('February','02',Dates1)
Dates3 = re.sub('March','03',Dates2)
Dates4 = re.sub('April','04',Dates3)
Dates5 = re.sub('May','05',Dates4)
Dates6 = re.sub('June','06',Dates5)
Dates7 = re.sub('July','07',Dates6)
Dates8 = re.sub('August','08',Dates7)
Dates9 = re.sub('September','09',Dates8)
Dates10 = re.sub('October','10',Dates9)
Dates11 = re.sub('November','11',Dates10)
Dates12 = re.sub('December','12',Dates11)    

print(Dates12)
print()

format1 = r'\d{6}'
format2 = r'\d\d/\d\d/\d\d\d\d'
format3 = r'\d\d \d\d, \d\d\d\d'

print(re.search(format1, Dates12).group())
print(re.search(format2, Dates12).group())
print(re.search(format3, Dates12).group())

# Better way to do these:
    
from datetime import datetime

# get current date
date2 = re.search(format2, Dates12).group()
print(date2)
print('Type :- ',type(date2))

# Create date object in given time format
my_date = datetime.strptime(date2, "%m/%d/%Y")

print(my_date)
print('Type: ',type(my_date))

print('Month: ', my_date.month) # To Get month from date
print('Year: ', my_date.year) # To Get month from year

# import calendar module
import calendar
print('Day of Month:', my_date.day)

# to get name of day(in number) from date
print('Day of Week (number): ', my_date.weekday())

# to get name of day from date
print('Day of Week (name): ', calendar.day_name[my_date.weekday()])

