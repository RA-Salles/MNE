"""
    31/03/23
    made by Locust, without other known aliases.


    This script tests the bissection method + some other major fuckery, such as autofinding good eval points 
"""

import numpy as np

def functioncreator(string):
    pass
def bissec(a:float ,b:float ,func,**kwarg) -> list: #useful for single root inside interval
    #INTIALIZATION BLOCK
    init = a
    finit = b
    precision: float = 0.1 #this guy makes the script stop. Very useful if you plan on having higher tolerances.
    if 'precision' in kwarg:
        try:
            precision = kwarg['precision']
        except:
            print("non floatable in precision. Reverted to standard.")
    else:
        pass
    exec: int = 1000
    i: int = -1
    if 'maxexecs' in kwarg:
        try:
            exec = kwarg['maxexecs']
        except:
            print("non number in exec kwarg. Reverted to standard")
    if func(init) * func(finit) <= 0:
        pass
        while abs(init-finit) > precision or i < exec:
            pass
    else:
        print("init-finit pair does not contain a 0.")
        return [0,0] #return 0, but in list.
    return [init,finit] #the bissec will return an interval instead of a

def bissecevaluator(func, n): #creates list of intervals to be evaluated. Works best when roots are closer to the y axis. For huge functions, make sure to make n big.
    #initialization block
    clusters = [] #this guy has no cap!!!! If your func got fucking 9000 roots in a step n proximity, better prepare for some ram consumption...
    yvals = [] #should store no more than 2 vals. shifts last val 
    pivot = n
    yvals = [func(0), func(n)]
    #FIRST RUN
    while len(clusters) == 0: #this guy runs until we hit the first root interval. Kind of a triple funny man.
        pivot += n #this guy is the step. It walk n units in the x axis and evaluates the function.
        if yvals[0]*yvals[1] <= 0:
            clusters.append(yvals)
        else:
            yvals[0] = yvals[1]
        yvals[1] = func(pivot) #already leaves iteration prepared for the next one, EVEN WHEN IT GOT A HIT.
        #if pivot/n > n*10000:
        #    break #unecessary. uncomment at will.
    #AFTER IT GOT THE FIRST HIT - it runs some more.
    for i in range(100):
        pivot += n #this guy is the step. It walk n units in the x axis and evaluates the function.
        if yvals[0]*yvals[1] <= 0:
            clusters.append(yvals)
        else:
            yvals[0] = yvals[1]
        yvals[1] = func(pivot) #already leaves iteration prepared for the next one, EVEN WHEN IT GOT A HIT.

    
    pass