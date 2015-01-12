from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

class Wunderground(WeatherResource):
    def getWeatherConditions(self, region, city):
        return {
            "a": 123,
        }
