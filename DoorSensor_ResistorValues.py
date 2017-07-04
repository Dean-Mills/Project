# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:43:02 2017

@author: deans
"""

RVals = [100.0,110.0,120.0,130.0,150.0,160.0,180.0,200.0,220.0,240.0,270.0,300.0,330.0,360.0,390.0,430.0,470.0,510.0,560.0,620.0,680.0,750.0,820.0,910.0,1000.0] #List of standard resistor values
R1 = 0 #Value for resistor 1
R2 = 0 #Value for resistor 2
ratio = 0 #Ratio found using R2/(R1 + R2) 
temp = [] #hold for the R1 and R2 values
Combinations = [] #Possible combinations that can be used
for x in range(len(RVals)):
    R2 = RVals[x]
    for y in range(len(RVals)):
        R1 = RVals[y]
        ratio = R2/(R1 + R2)
        ratio = ratio - 0.66 
        if((ratio < 0.01)and(ratio > -0.01)):
            temp.append(R1)
            temp.append(R2)
            Combinations.append(temp)
            temp = []
print "Resistor values under ideal circumstances"
for x in range(len(Combinations)):
    print "R1: " + repr(Combinations[x][0]) + "       " + "R2: " +     repr(Combinations[x][1])    
    
    
R1 = 0 #Value for resistor 1
R2 = 0 #Value for resistor 2
ratio = 0 #Ratio found using R2/(R1 + R2) 
temp = [] #hold for the R1 and R2 values
Combinations = [] #Possible combinations that can be used
for x in range(len(RVals)):
    R2 = RVals[x] - (RVals[x] * 0.05)
    for y in range(len(RVals)):
        R1 = RVals[y] - (RVals[y] * 0.05)
        ratio = R2/(R1 + R2)
        ratio = ratio - 0.66 
        if((ratio < 0.01)and(ratio > -0.01)):
            temp.append(RVals[y])
            temp.append(RVals[x])
            Combinations.append(temp)
            temp = []
print "Resistor values under simulated practical circumstances"
for x in range(len(Combinations)):
    print "R1: " + repr(Combinations[x][0]) + "       " + "R2: " +     repr(Combinations[x][1])
    
R1 = 0 #Value for resistor 1
R2 = 0 #Value for resistor 2
ratio = 0 #Ratio found using R2/(R1 + R2) 
temp = [] #hold for the R1 and R2 values
Combinations = [] #Possible combinations that can be used
for x in range(len(RVals)):
    R2 = RVals[x] - (RVals[x] * 0.05)
    for y in range(len(RVals)):
        R1 = RVals[y] - (RVals[y] * 0.05)
        ratio = R2/(R1 + R2)
        ratio = ratio - 0.66 
        if((ratio < 0.01)and(ratio > -0.01)):
            temp.append(RVals[y])
            temp.append(RVals[x])
            Combinations.append(temp)
            temp = []
print "Resistor values under simulated practical circumstances"
for x in range(len(Combinations)):
    print "R1: " + repr(Combinations[x][0]) + "       " + "R2: " +     repr(Combinations[x][1])