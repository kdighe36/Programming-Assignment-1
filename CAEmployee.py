import unittest

class Employee:
    stdrate = 0.2
    highrate = 0.4
    prsi = 0.04
    def __init__(self, StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.StaffID = StaffID
        self.LastName = LastName
        self.FirstName = FirstName
        self.RegHours = RegHours
        self.HourlyRate = HourlyRate
        self.OTMultiple = OTMultiple
        self.TaxCredit = TaxCredit
        self.StandardBand = StandardBand

    def computePayment(self,workedhours,date):
        result = {}
        name = self.FirstName+" "+self.LastName
        result["name"] = name
        result["date"] = date
        result["Regular Hours Worked"] = workedhours
        if workedhours > self.RegHours:
            overtimehoursworked = workedhours - self.RegHours
        else:
            overtimehoursworked = 0
        result["Overtime Hours Worked"] = overtimehoursworked
        result["Regular Rate"] = self.HourlyRate
        overtimerate = self.OTMultiple * self.HourlyRate
        result["Overtime Rate"] = overtimerate
        regularpay = self.RegHours * self.HourlyRate
        result["Regular Pay"] = regularpay
        overtimepay = overtimerate * overtimehoursworked
        result["Overtime Pay"] = overtimepay
        grosspay = overtimepay + regularpay
        result["Gross Pay"] = grosspay
        result["Standard Rate Pay"] = self.StandardBand
        higherratepay = grosspay - self.StandardBand
        result["Higher Rate Pay"] = higherratepay
        standardtax = self.StandardBand * self.stdrate
        result["Standard Tax"] = standardtax
        highertax = higherratepay * self.highrate
        result["Higher Tax"] = highertax
        totaltax = standardtax + highertax
        result["Total Tax"] = totaltax
        result["Tax Credit"] = self.TaxCredit
        nettax = totaltax - self.TaxCredit
        result["Net Tax"] = round(nettax,1)
        PrsiTax = grosspay * self.prsi
        result["PRSI"] = PrsiTax
        netdeductions = nettax + PrsiTax
        result["Net Deductions"] = round(netdeductions, 1)
        netpay = grosspay-netdeductions
        #calculated net pay
        result["Net Pay"] = netpay
        return result

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
print(jg.computePayment(42,'31/10/2021'))


class TestcasesForEmployee(unittest.TestCase):

    #Net pay cannot exceed gross pay
    def testNetLessEqualGross(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.computePayment(1, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

    # Test overtime is 0
    def testOvertimeisZero(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(1, '31/10/2021')
        self.assertEqual(pi["Overtime Pay"], 0)

    #Test Regular hours worked cannot exceed worked hours
    def testreghrslesswrk(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertGreaterEqual(pi['Regular Hours Worked'], 37)

    #Test Net Pay cannot be negative
    def testnetpay(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(0, '31/10/2021')
        self.assertGreaterEqual(pi["Net Pay"], 0)








