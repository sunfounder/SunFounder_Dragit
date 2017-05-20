from basic import _Basic_class
import requests
import json

class Weather(object):
	"""
	get weather message from internet
	http://openweathermap.org/
	"""
	city        = None
	API_key     = None
	url         = None
	
	_city_name   = 'N/A'
	_weather     = 'N/A'
	_temp        = 'N/A'
	_temp_min    = 'N/A'
	_temp_max    = 'N/A'
	_humidity    = 'N/A'
	_pressure    = 'N/A'
	_wind_speed  = 'N/A'
	_wind_degree = 'N/A'


	def __init__(self, city, API_key):
		super(Weather, self).__init__()
		if city == None or API_key == None:
			raise ValueError ("city or API_key is None")
		else:
			self.city    = city
			self.API_key = API_key
			self.url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s'%(self.city, self.API_key)

	def reflash(self):
		jsonStr     = requests.get(self.url).text
		
		data        = json.loads(jsonStr)

		self._city_name   = data["name"]
		self._weather     = data["weather"][0]["description"]
		self._temp        = float(data["main"]["temp"])-273.16
		self._temp_min    = float(data["main"]["temp_min"])-273.16
		self._temp_max    = float(data["main"]["temp_max"])-273.16
		self._humidity    = float(data["main"]["humidity"])
		self._pressure    = float(data["main"]["pressure"])
		self._wind_speed  = float(data["wind"]["speed"])
		self._wind_degree = float(data["wind"]["deg"])
'''
		print"++++++++++++++++++++++++++++++++++++"
		print"weather report:\n"
		print "    city :", self._city
		print "    weather:", self._weather
		print "    temp:", self._temp
		print "    temp_min:", self._temp_min
		print "    temp_max:", self._temp_max
		print "    humidity:", self._humidity
		print "    pressure:", self._pressure
		print "    wind speed:", self._wind_speed
		print "    wind_degree:", self._wind_degree
		print "++++++++++++++++++++++++++++++++++++"
'''
@property
def weather(self):
    return self._weather

@property
def temperature(self):
    return self._temp

@property
def temp_min(self):
    return self._temp_min

@property
def temp_max(self):
    return self._temp_max

@property
def city(self):
    return self._city
