import sys, getopt

from flask import Flask
from flask.ext import restful

from config import routing

app = Flask(__name__)
api = restful.Api(app)

routing.registerRoutes(api)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:p:e:", ["host=", "port=", "env="])
    except getopt.GetoptError:
        print 'app.py [-h <host=0.0.0.0>] [-p <port=5000>] [-e <env=prod|dev>]'
        sys.exit(2)
    
    server_options = {
        'host': "0.0.0.0",
        'port': 5000,
        'env': "prod",
        'debug': False
    }
    
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            server_options['host'] = arg
        elif opt in ("-p", "--port"):
            server_options['port'] = int(arg)
        elif opt in ("-e", "--env"):
            server_options['env'] = arg
    
    server_options['debug'] = server_options['env'].lower() == 'dev'
    
    app.run(
        host=server_options['host'],
        port=server_options['port'],
        debug=server_options['debug']
    )

if __name__ == "__main__":
    main(sys.argv[1:])
