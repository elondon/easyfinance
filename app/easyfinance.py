import json
import logging
import os

from flask_cors import CORS
from http.client import HTTPException
from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import abort, default_exceptions

path = os.path.dirname(os.path.abspath(__file__))
api_root = '/easyfinance/api/v1'


def make_json_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code
                            if isinstance(ex, HTTPException)
                            else 500)
    return response


# todo environments, config files, etc...

app = Flask(__name__)
cors = CORS(app, resources={r"/easyfinance/api/v1/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://svceasyfinance:welcome@localhost/easyfinance'

# make all errors return json.
for code in default_exceptions.keys():
    app.error_handler_spec[None][code] = make_json_error

# logging
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler(path + '/access.log')

if app.debug is True:
    app.logger.setLevel(logging.DEBUG)
    logging.getLogger().setLevel(logging.DEBUG)

    logger.addHandler(handler)
    app.logger.addHandler(handler)
else:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.INFO)


@app.route(api_root + '/helloworld', methods=['GET'])
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', passthrough_errors=True)
