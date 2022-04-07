

class Employee:

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
        overtimehoursworked = workedhours - self.RegHours
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
        higherratepay = grosspay- self.StandardBands
        result["Higher Rate Pay"] = higherratepay
        standardtax = self.StandardBand * self.stdrate
        result["Standard Tax"] = standardtax
        highertax = higherratepay * self.highrate
        result["Higher Tax"] = highertax
        totaltax = standardtax + highertax
        result["Total Tax"] = totaltax
        result["Tax Credit"] = self.TaxCredit
        nettax = totaltax - self.TaxCredit
        result["Net Tax"] = nettax
        PrsiTax = grosspay * self.prsi
        result["PRSI"] = PrsiTax
        netdeductions = nettax + PrsiTax
        result["Net Deductions"] = netdeductions
        netpay = grosspay-netdeductions
        result["Net Pay"] = netpay
        return result








