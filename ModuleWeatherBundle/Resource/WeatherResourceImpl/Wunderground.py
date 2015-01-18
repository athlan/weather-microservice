from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

import urllib
import urllib2
import json

class Wunderground(WeatherResource):
    def __init__(self, parameters):
        
        self.api_key = parameters.wunderground_api_key
        
        super(Wunderground, self).__init__()
    
    def getWeatherConditions(self, region, city):
        
        url = 'http://api.wunderground.com/api/%s/conditions/q/%s/%s.json' % (self.api_key, region, city)

        print "Fetching weather from %s" % url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        
        data = json.loads(the_page)
        
        return data
