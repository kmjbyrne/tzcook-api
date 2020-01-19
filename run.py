__author__ = 'kmjb'

import sys

from app import create_app

if __name__ == '__main__':
    app = None
    if len(sys.argv) > 1:
        app = create_app(sys.argv[1])
    else:
        app = create_app('DEV')
    app.run(port=app.config['RUN_PORT'], debug=True, host='0.0.0.0')
