from ModuleWeatherBundle.Resource.WeatherResource import WeatherResource

import json

class Cached(WeatherResource):
    def __init__(self, service, cache_redis, cache_ttl = 3600):
        super(Cached, self).__init__()
        
        self.service = service
        self.cache_redis = cache_redis
        self.cache_ttl = cache_ttl
    
    def getWeatherConditions(self, region, city):
        key_params = {
            'method': 'conditions',
            'region': region,
            'city': city,
        }
        key = 'wunderground_' + json.dumps(key_params, separators=(',', ':'))
        
        data = self.cache_redis.get(key)
        
        if data is not None:
            return json.loads(data)
        
        data = self.service.getWeatherConditions(region, city)
        
        self.cache_redis.set(
            key,
            json.dumps(data),
            self.cache_ttl
        )
        
        return data
