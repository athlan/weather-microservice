from flask.ext import restful

import ModuleWeatherBundle.Resource.WeatherResourceImpl.Wunderground

class WeatherController(restful.Resource):
    def get(self):
        service = ModuleWeatherBundle.Resource.WeatherResourceImpl.Wunderground.Wunderground()
        data = service.getWeatherConditions("a", "b")
        
        return data
