import redis

class RedisConnection(object):
    def __init__(self, options):
        if not isinstance(options, dict):
            options = {}
        
        host = options.get('host', 'localhost')
        port = options.get('port', 6379)
        db = options.get('db', 0)
        
        self.redis = redis.StrictRedis(host, port, db)

    def connection(self):
        return self.redis
    