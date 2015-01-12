from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

class Wunderground(WeatherResource):
    def __init__(self, arg1):
        
        self.arg1 = arg1
        
        super(Wunderground, self).__init__()
    
    def getWeatherConditions(self, region, city):
        return {
            "a": self.arg1,
        }
