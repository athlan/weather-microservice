from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

from datetime import datetime

class WundergroundApiLimitGuard(WeatherResource):
    def __init__(self, service, cache_redis, per_10_min_limit = 10, per_day_limit = 500):
        super(WundergroundApiLimitGuard, self).__init__()
        
        self.service = service
        self.cache_redis = cache_redis
        self.per_10_min_limit = per_10_min_limit
        self.per_day_limit = per_day_limit
    
    def getWeatherConditions(self, region, city):
        self.checkLimit()
        
        return self.service.getWeatherConditions(region, city)
    def checkLimit(self):
        
        key_prefix_10min = 'wunderground_request_log_10min_'
        key_prefix_day = 'wunderground_request_log_day_'
        
        requests_num = len(self.cache_redis.keys(key_prefix_10min + '*'))
        if requests_num >= self.per_10_min_limit:
            raise RuntimeWarning("Limit of %s requests per 10min exceeded with %s " % (self.per_10_min_limit, requests_num))
        
        requests_num = len(self.cache_redis.keys(key_prefix_day + '*'))
        if requests_num >= self.per_day_limit:
            raise RuntimeWarning("Limit of %s requests per day exceeded with %s " % (self.per_day_limit, requests_num))
        
        now = datetime.now()
        
        key = '%s_%s' % (key_prefix_10min, now.isoformat())
        self.cache_redis.set(key, '1', 10 * 3600)
        
        key = '%s_%s' % (key_prefix_day, now.isoformat())
        self.cache_redis.set(key, '1', 24 * 60 * 3600)
        