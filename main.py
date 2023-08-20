#!/bin/python3
# Day Counter
# Written by: Nick Lueth
# 8/20/2023

from calendar import isleap 

dict_months = {"january":31, "february":28, "march":31, "april": 30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}

list_months = list(dict_months.values())

start = "6/6/1944"
end = "8/20/2023"


def date_convert(date):
    date_str = date.split("/")
    new_date = []
    
    for item in date_str:
        new_date.append(int(item))
    return new_date


def get_days(start_date, end_date):
    num_days = 0
    if (start_date[2] > end_date[2]) or (start_date[2] == end_date[2] and start_date[0] > end_date[0]) or (start_date[2] == end_date[2] and start_date[0] == end_date[0] and start_date[1] > end_date[1]):
        print("Invalid dates!")
        exit(0)
    else:
        while start_date != end_date:
            if isleap(start_date[2]):
                list_months[1] = 29
            else: 
                list_months[1] = 28
            if start_date[1]+1 > list_months[start_date[0]-1]:
                if start_date[0]+1 > 12:
                    start_date[2] += 1
                    start_date[0] = 1
                    start_date[1] = 1
                    num_days += 1
                else:
                    start_date[0] += 1
                    start_date[1] = 1
                    num_days += 1
            else:
                start_date[1] += 1
                num_days += 1
    return num_days

print("It will take", get_days(date_convert(start), date_convert(end)), "days to go from", start, "to", end)
