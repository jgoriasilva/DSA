"""
Given two arrays like 

a = [[10:30, 13:00], [13:00, 13:15], [14:00, 15:00], [16:30, 18:00]]
b = [[09:00, 10:00], [11:00, 11:15], [11:30, 12:00], [14:00, 15:00], [16:15, 17:30]]

and availabilities

c = [08:30, 19:00]
d = [09:00, 17:45]

find availabilities for meetings


Idea:

Brute force:

Calculate actual availabilities = [max(), min()]

Function to convert str hour to int = 


Algorithm:

Have a counter of time variable
Start it at actual availability.
Have two pointers, one for each a, b.
While current time < actual availabilitie:
    access positions of arrays
    if both values are bigger than current time variable
        availabilities append [current time, min(first meeting start)]
        current time = end of meeting that started first
        update pointer of corresponding array
    else:
        if a < current time:
            current time = end of meeting of a
            update pointer of a
        if b < current time:
            current time = end of meeting of b
            update pointer of b
"""

from typing import *

def convert_hour_str_int(hour: str) -> int:
    h, m = map(int,hour.split(':'))

    return h*60+m

def convert_hour_int_str(hour: int) -> str:

    h = int(hour/60)
    m = hour - h*60

    return f'{h:00}:{m:00}'


def find_availabilities(meet_1: List[List[str]], meet_2: List[List[str]], avail_1: List[str], avail_2: List[str], duration: int) -> List[List[str]]:

    availabilities = []
    # [[10:00, 10:30], ]

    avail_1_2 = [max(convert_hour_str_int(avail_1[0]), convert_hour_str_int(avail_2[0])), \
                 min(convert_hour_str_int(avail_1[1]), convert_hour_str_int(avail_2[1]))]
    # [09:00, 17:45]
    
    current_time = avail_1_2[0]
    # 13:15 

    p_meet_1, p_meet_2 = 0, 0
    # 2, 1
    # len 4, 5


    while current_time < avail_1_2[1] and p_meet_1 < len(meet_1) and p_meet_2 < len(meet_2):
        start_1, start_2 = convert_hour_str_int(meet_1[p_meet_1][0]), convert_hour_str_int(meet_2[p_meet_2][0])
        # 14:00, 11:00
        
        end_1, end_2 = convert_hour_str_int(meet_1[p_meet_1][1]), convert_hour_str_int(meet_2[p_meet_2][1])
        # 15:00, 11:15

        if start_1 - current_time >= duration and start_2 - current_time >= duration:
            if start_1 < start_2:
                availabilities.append(list(map(convert_hour_int_str,[current_time, start_1])))
                current_time = end_1
                p_meet_1 += 1
            else:
                availabilities.append(list(map(convert_hour_int_str,[current_time, start_2])))
                current_time = end_2
                p_meet_2 += 1
        else:
            if start_1 - current_time < duration:
                current_time = max(end_1, current_time)
                p_meet_1 += 1
            if start_2 - current_time < duration:
                current_time = max(end_2, current_time)
                p_meet_2 += 1
        

    return availabilities


a = [["10:30", "13:00"], ["13:00", "13:15"], ["14:00", "15:00"], ["16:30", "18:00"]]
b = [["09:00", "10:00"], ["11:00", "11:15"], ["11:30", "12:00"], ["14:00", "15:00"], ["16:15", "17:30"]]

c = ["08:30", "19:00"]
d = ["09:00", "17:45"]


availabilities = find_availabilities(a, b, c, d, 5)

print(availabilities)