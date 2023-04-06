from functools import lru_cache
from flask import Flask, abort, request, Response

from statapi import methods
from statapi.methods import formatters

from utils import get_docstring, to_bool

app = Flask(__name__)


@app.route('/stats/')
def stats_root():
    ret = {'methods': list(methods)}

    format = request.args.get('format')
    
    if format:
        doc_format = methods.formatters.get('format')[1]
        return doc_format(ret)

    ret['response'] = [f"<h2>#{i} | {obj}</h2>  <p>{get_docstring(obj)}</p>" for i, obj in enumerate(ret['methods'], start=1)]
    return Response(ret['response'])


@app.route('/stats/<string:method>')
def stats(method):
    format = request.args.get('format')
    if format not in formatters:
        abort(415, f"Invalid format parameter\nPossible format types are: {', '.join(formatters)}")

    kwargs = request.args.to_dict()
    kwargs = to_bool(**kwargs)

    try:
        func = methods[method]
    except KeyError:
        abort(404, f'Method {method} not found')

    try:
        res, mime = func(**kwargs)
    except ValueError as exc:
        abort(404, exc)

    

    return Response(res, mimetype=mime)


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    import logging
    app.logger.setLevel(logging.DEBUG)

    # (!) Never run your app on '0.0.0.0 unless you're deploying
    #     to production, in which case a proper WSGI application
    #     server and a reverse-proxy is needed
    #     0.0.0.0 means "run on all interfaces" -- insecure
    app.run(host='127.0.0.1', port=5000, debug=True)
