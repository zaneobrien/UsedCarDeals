from edmunds import Edmunds
from craigslist import CraigslistForSale
import json


class UsedCar(object):
    def EdmundCall(self):
        """Makes an API call to Edmunds and puts response from json into a dictionary"""
        # get styleID by the make model and year of car
        api = Edmunds('#YOUR_KEY_HERE')
        styleIDResponse = api.make_call('/api/vehicle/v2/'+self.make+'/'+self.model+'/'+self.year+'/styles')
        styleIDJson = json.dumps(styleIDResponse)
        styleIDDict = json.loads(styleIDJson)
        # extract the correct styleID for the corresponding make,model,year
        for i in styleIDDict['styles']:
            if self.trim == i['trim']:
                self.id = i['id']
                break

        response = api.make_call('/v1/api/tmv/tmvservice/calculateusedtmv', styleId=self.id,condition=self.condition,mileage=self.mileage, zip=self.zipcode)
        carPriceJson = json.dumps(response)
        carPriceDict = json.loads(carPriceJson)
        self.usedprice = carPriceDict["tmv"]["totalWithOptions"]["usedPrivateParty"]
        print ('Price for used '+ self.year +' '+ self.make +' '+ self.model + ' '+ self.trim + ' with '+ self.mileage+ ' miles')
        print (carPriceDict["tmv"]["totalWithOptions"]["usedPrivateParty"])

    def CraigslistCompare(self):
        """Uses CraigsList scraper to search deals in the area and gets price"""
        CraigslistCar = CraigslistForSale(category='cta', site=self.city,filters={'query':self.year +' '+ self.make +' '+ self.model +' '+ self.trim})
        print 'Searching Craigslist: ' + self.year +' '+ self.make +' '+ self.model + ' '+ self.trim
        for result in CraigslistCar.get_results(limit=5):
            #take off '$'
            dollarPrice = result["price"]
            actualprice = float(dollarPrice[1:])
            if actualprice < self.usedprice:
                print ('Good deal: ' + result["name"] +'    '+ result["price"]+ '   ' + result['url'])
            elif actualprice < (.9*self.usedprice):
                print ('Great deal: ' + result["name"] +'    '+ result["price"]+ '   ' + result['url'])
            elif actualprice < (.8*self.usedprice):
                print ('Fantastic deal: ' + result["name"] +'    '+ result["price"]+ '   ' + result['url'])
            elif actualprice < (.7*self.usedprice):
                print ('This is a Steal! : ' + result["name"] +'    '+ result["price"]+ '   ' + result['url'])
            else:
                print ('Bad deal! : ' + result["name"] +'    '+ result["price"]+ '   ' + result['url'])

    def __init__(self,make,model,year,trim,mileage,condition,city,zipcode):
        self.make = make
        self.model = model
        self.year = year
        self.trim = trim
        self.mileage = mileage
        self.condition = condition
        self.city = city
        self.zipcode = zipcode

Car = UsedCar('#make','#model','#year','#trim','#miles','#condition','#city','#zipcode')
Car.EdmundCall()
Car.CraigslistCompare()
