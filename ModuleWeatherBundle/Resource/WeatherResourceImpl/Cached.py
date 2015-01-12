from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

class Cached(WeatherResource):
    def __init__(self, service, cache_redis, cache_ttl = 3600):
        super(Cached, self).__init__()
        
        self.service = service
        self.cache_redis = cache_redis
        self.cache_ttl = cache_ttl
    
    def getWeatherConditions(self, region, city):
        return self.service.getWeatherConditions(region, city)
