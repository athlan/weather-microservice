from ModuleWeatherBundle.Controller.WeatherController import WeatherController

def registerRoutes(api):
    api.add_resource(WeatherController, '/api/v1.0/')
