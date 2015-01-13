from ModuleWeatherBundle.Controller.WeatherController import WeatherController

def registerRoutes(api, container):
    
    controller = WeatherController
    controller.container = container
    api.add_resource(controller, '/api/v1.0/weather/conditions/<string:region>/<string:city>')
