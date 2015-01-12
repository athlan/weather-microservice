from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

class Wunderground(WeatherResource):
    def __init__(self, parameters):
        
        self.api_key = parameters.wunderground_api_key
        
        super(Wunderground, self).__init__()
    
    def getWeatherConditions(self, region, city):
        return {
            "a": self.api_key,
        }
