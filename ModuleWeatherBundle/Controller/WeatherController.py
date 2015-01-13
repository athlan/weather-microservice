from flask.ext import restful

import ModuleWeatherBundle.Resource.WeatherResourceImpl.Wunderground

class WeatherController(restful.Resource):
    def get(self, region, city):
        service = self.container.get_object('WeatherResource')
        data = service.getWeatherConditions(region, city)
        
        response = {}
        response["query"] = {
            "region": region,
            "city": city,
        }
        
        if "error" in data["response"]:
            response["error"] = data["error"]
            return response, 400
        
        response["data"] = data
        
        return response
