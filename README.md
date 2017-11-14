# UsedCarPrices

Searching for a new car? use this!

### Running

1) Clone from github, making sure you use the --recursive flag in order to grab the sub modules

``` git clone https://github.com/zaneobrien/UsedCarPrices.git --recursive ```

2) Give Inputs

Get and API key for Edmunds API
[Edmunds](http://developer.edmunds.com/ "Here")

Fill in API Key
```python
api = Edmunds('#YOUR_KEY_HERE')
```

Fill in information here
```python
Car = UsedCar('#make','#model','#year','#trim','#miles','#condition','#city','#zipcode')
```
