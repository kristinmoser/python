



BASE_HOURLY_PAY_RATE = 17.22
NEGATIVE_HOURS_ERROR = 0
PAY_RATE_NEG_ERROR = 1


class Worker():
    def __init__(self, SSN):
        self.__SSN = SSN
    def setHourlyRate(self, rate = BASE_HOURLY_PAY_RATE):
        if rate > 0:
            self.__hourlyRate = rate
        #else:
            #return PAY_RATE_NEG_ERROR
    def setTitle(self,title):
        self.__title = ' '
    def setHours(self, hoursWorked):
        self.__hoursWorked = 0
        if hoursWorked > 0:
            self.__hoursWorked += hoursWorked
        #else:
           # return NEGATIVE_HOURS_ERROR
        return self.__hoursWorked
    def calcWages(self, hoursWorked,hourlyPayRate):
        self.__paycheck = self.__hoursWorked * self.__hourlyPayRate
        

'''SSN which uniquely identifies the worker
hourly pay rate (there is no overtime)
everyone in this company starts with $17.22 per hour
this may be changed at any time (performance reviews and all that)
when it's time to get paid, whatever the current hourly pay rate is
     is used to calculate the pay amount for the period since the last payment
as always, your code must enforce that no bad changes are made to this and every data member
     errors like negative amounts or amounts over the maximum allowed as set by a company (see below)
     use the "return an error code" methodology instead of the "raise an exception" methodology for this
     (especially since we didn't cover creating and raising your own exceptions)
hours worked since last getting paid
again, take responsibility for dumb changes and don't let them happen using the same methodolgy
also take responsibility for not paying any worker more than they should get
a possible title - to be awarded after being earned
no worker starts with a title when hired
the title doesn't affect the pay but after being awarded, it is used as part of their payment report
the title might also be changed at some future point.'''        
