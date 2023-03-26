from flask import Flask, jsonify
from datetime import datetime, timedelta

from utils import validate_timezone, get_docstring

app = Flask(__name__)


@app.route('/datetime', strict_slashes=False)
def get_datetime():
    """
    This endpoint returns current datetime with optional timezone offset.

    Parameters:
        offset (int): The timezone offset in hours [-12, -11, ..., +11, +12].

    Returns:
        str: The current datetime in ISO format.

    Examples:
        >>> import requests
        >>> response = requests.get('/datetime')
        >>> response.status_code
        200
        >>> response.content
        b'2023-03-26T12:00:00.000000Z'
    """
    app.logger.info('You are on documentation route')
    
    return get_docstring(get_datetime)

    # server_datetime = datetime.utcnow()
    # return jsonify({'datetime': server_datetime})


@app.route('/datetime/')
@app.route('/datetime/<string:timezone_offset>')
def get_datetime_with_timezone_offset(timezone_offset=0):
    app.logger.info(f'You are on GMT({timezone_offset}) time zone')

    timezone_offset_int = int(timezone_offset)
    validate_timezone(timezone_offset_int)

    server_datetime = datetime.utcnow() + timedelta(hours=timezone_offset_int)
    return f"Time in GMT{timezone_offset} is {server_datetime}"

    # return jsonify({'datetime': server_datetime})


if __name__ == '__main__':
    import logging
    app.logger.setLevel(logging.DEBUG)

    app.run(host='127.0.0.1', port=8000, debug=True)
