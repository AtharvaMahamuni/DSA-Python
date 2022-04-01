class PropertyDealer:

    regNo
    deals = []

    def __init__(self, regNo, deals):
        self.regNo = regNo
        self.deals = deals


propertyDealerList = []

num = int(input())

for i in range(num):

    regNo = int(input())
    dealsNo = int(input())

    deals = []

    for j in range(dealsNo):
        propertyType = input()
        rateOfCommision = int(input())
        deals.append((propertyType, rateOfCommision))

    propertyDealerList.append(PropertyDealer(regNo, deals))