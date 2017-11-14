# UsedCarPrices

Searching for a new car? use this!

### Prep

1) Clone from github, making sure you use the --recursive flag in order to grab the sub modules

``` git clone https://github.com/zaneobrien/UsedCarPrices.git --recursive ```

2) Give Inputs

Get and API key at [Edmunds API](http://developer.edmunds.com/ "Here")

Fill in API Key in UsedCarPrices.py
```python
api = Edmunds('#YOUR_KEY_HERE')
```

Fill in information in UsedCarPrices.py
```python
Car = UsedCar('#make','#model','#year','#trim','#miles','#condition','#city','#zipcode')
```

### Running

Will work with python 2 or 3

``` python UsedCarPrices.py```
