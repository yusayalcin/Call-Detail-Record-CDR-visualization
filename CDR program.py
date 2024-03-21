import matplotlib.pyplot as plt
from CDRLib import *


name = "AnonymizedCDR.csv" 

myList = readCSV(name)

data=[makecall(i) for i in myList]  


end = "y"
while end =="y":
    ans = input("Please choose one: (A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P)?")
    if ans == "A":
        disposition(data)
    elif ans == "B":
        ERRbyzone(data)
    elif ans == "C":
        call_by_time(data)
    elif ans == "D":
        call_by_day(data)
    elif ans == "E":
        total_call_duration(data)
    elif ans == "F":
        errcode(data)
    elif ans == "G":
        callmonth(data)
    elif ans == "H":
        callcountry(data)
    elif ans == "I":
        country(data)
    elif ans == "J":
        dispositionsInAday(data)
    elif ans == "K":
        prefix(data)
    elif ans == "L":  
        trunk(data)
    elif ans == "M":
        src(data)
    elif ans == "N":
        group_id(data)
    elif ans == "O":   
        BYEbyzones(data)
    elif ans == "P":
        calldir(data)
    
    end=input("\n keep analyzing (y/n): ")

