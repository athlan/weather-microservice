from flask.ext import restful

import ModuleWeatherBundle.Resource.WeatherResourceImpl.Wunderground

class WeatherController(restful.Resource):
    def get(self, region, city):
        service = self.container.get_object('WeatherResource')
        
        response = {}
        response["query"] = {
            "region": region,
            "city": city,
        }
        
        try:
            data = service.getWeatherConditions(region, city)
        except (Exception) as e:
            response["error"] = str(e)
            return response, 400
        
        if "response" in data:
            if "error" in data["response"]:
                response["error"] = data["error"]
                return response, 400
        
        response["data"] = data
        
        return response
