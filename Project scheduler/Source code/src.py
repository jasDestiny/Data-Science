#Made by John Arthur Samuel D
#All rights reserved ©2020

import pandas as pd

fileName=str(input("Please enter file name"))
rf=pd.read_csv(fileName)

#sparation of morning and afternoon slots
colName=str(input("Enter column name that identifies slot"))
val=str(input("Enter value that identifies morning batch"))
afternoon=rf[rf[colName]!=val]
morning=rf[rf[colName]==val]

#printing to check
afternoon
morning

#creating list to set as columns
t=int(input("How much time per day"))
tt=int(input("How much time per team(Note: Make sure it is a factor of previous input value)"))
n=int(t/tt)
days=[i for i in range(1,100,1) for j in range(1,n+1,1)]
status=["Not yet done" for i in range(1,100,1)]
startingTime=[i for j in range(0,100,1) for i in range(0,t,tt)]
endingTime=[i+5 for j in range(0,100,1) for i in range(0,t,tt)]

#code to add 2 new columns
afternoon["Day number"]=days[0:len(afternoon)]
morning["Day number"]=days[0:len(morning)]
afternoon["Starting time(in mins)"]=startingTime[0:len(afternoon)]
afternoon["Ending time(in mins)"]=endingTime[0:len(afternoon)]
morning["Starting time(in mins)"]=startingTime[0:len(morning)]
morning["Ending time(in mins)"]=endingTime[0:len(morning)]
morning["Status"]=status[0:len(morning)]
afternoon["Status"]=status[0:len(afternoon)]

#exporting them to csv
afternoon.to_csv("afternoon.csv")
morning.to_csv("morning.csv")
