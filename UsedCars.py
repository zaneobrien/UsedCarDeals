from edmunds import Edmunds
from craigslist import CraigslistForSale
import json


class UsedCar(object):

#make_call('/v1/api/vehiclephoto/service/findphotosbystyleid', comparator='simple', styleId='3883')
#https://api.edmunds.com/v1/api/tmv/tmvservice/calculateusedtmv?styleid=100001210&condition=Outstanding&mileage=25000&zip=90069&fmt=json&api_key=8tx5sraszgugftzfu2rtdpbw
    def Edmondresponse(self):
        """put json into a dictionary"""

        #get styleID by the make model and year of car
        api = Edmunds('8tx5sraszgugftzfu2rtdpbw') # use Edmunds('YOUR API KEY', True) for debug mode
        styleidResponse = api.make_call('/api/vehicle/v2/ford/f150/2011/styles')
        styleIDJson = json.dumps(styleidResponse)
        styleIDDict = json.loads(styleIDJson)
        #extract the correct styleID for the correcponding make,model,year
        #for key in styleIDDict.items():
        #    if key = self.
        #    print key



        #print styleIDDict["styles"][0]
        #self.styleid = styleIDDict[]
        #print styleIDJson
        #self.styleID
        #print styleidResponse


        response = api.make_call('/v1/api/tmv/tmvservice/calculateusedtmv', styleId='101353967',condition=self.condition,mileage=self.mileage, zip=self.zipcode)
        carJson = json.dumps(response)
        carDict = json.loads(carJson)
        self.usedprice = carDict["tmv"]["totalWithOptions"]["usedPrivateParty"]
        print ('-----Used Price-----')
        print (carDict["tmv"]["totalWithOptions"]["usedPrivateParty"])

    def Craigslist(self):
        """uses CraigsList scraper to see if the car is availible"""
        #print CraigslistForSale.show_filters(category='cta')


    #def ComparePrice(self):


    def __init__(self,make,model,year,mileage,condition,zipcode):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
        self.zipcode = zipcode

Car = UsedCar('ford','f150','2011','150000','Outstanding','92024')
Car.Edmondresponse()
Car.Craigslist()
