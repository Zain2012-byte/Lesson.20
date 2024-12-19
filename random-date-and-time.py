import random

import time

def getRandomDate(StartDate,EndDate):

    print("Printing random date between",StartDate,"and ",EndDate)

    randomgenerator= random.random()

    dateformat= '%m/%d/%Y' 

    starttime=time.mktime(time.strptime(StartDate,dateformat))
    endtime= time.mktime(time.strptime(EndDate,dateformat))

    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))

    return randomdate
print("rndom date=",getRandomDate('1/1/2020','12/12/2024'))
