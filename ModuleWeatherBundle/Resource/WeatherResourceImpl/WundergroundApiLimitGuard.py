from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

class WundergroundApiLimitGuard(WeatherResource):
    def __init__(self, service, cache_redis, per_10_min_limit = 10, per_day_limit = 500):
        super(WundergroundApiLimitGuard, self).__init__()
        
        self.service = service
        self.cache_redis = cache_redis
        self.per_10_min_limit = per_10_min_limit
        self.per_day_limit = per_day_limit
    
    def getWeatherConditions(self, region, city):
        
        ''' TODO: count requests and prevent limits '''
        
        return self.service.getWeatherConditions(region, city)
