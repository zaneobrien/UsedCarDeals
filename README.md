# Used Car Deals

Searching for a used car? use this!

This program compares prices from Edmunds used car data with active listings on Craigslist in order to find great deals on Craigslist.

### Prep

1) Clone from github, making sure you use the --recursive flag in order to grab the sub modules

      ``` git clone https://github.com/zaneobrien/UsedCarDeals.git --recursive ```

2) Give Inputs

      Get and an API key at [Edmunds API](http://developer.edmunds.com/ "Here")
      ***Edmonds is stopping their public API access as of Feb 2017***

      Fill in API Key in secrets.py
   ```python
   api = "YOUR_KEY_HERE"
   ```

      Fill in car information in UsedCarPrices.py
   ```python
   Car = UsedCar('#make','#model','#year','#trim','#miles','#condition','#city','#zipcode')
   ```

### Running

This will work with python 2 or 3

``` python UsedCarPrices.py```
