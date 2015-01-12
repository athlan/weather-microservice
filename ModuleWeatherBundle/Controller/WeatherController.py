from flask.ext import restful

import ModuleWeatherBundle.Resource.WeatherResourceImpl.Wunderground

class WeatherController(restful.Resource):
    def get(self):
        
        service = self.container.get_object('WeatherResource')
        data = service.getWeatherConditions("a", "b")
        
        return data
