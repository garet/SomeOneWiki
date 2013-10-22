'''
Created on 25 сент. 2013 г.

@author: garet
'''
import json

from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import unquote
from urllib.parse import quote

from flask import Flask, redirect, request, url_for


app = Flask(__name__)

@app.route('/ajax/', defaults={'path': ''})
@app.route('/ajax/<path:path>')
def ajax_handler(path):
    result = 'ST: %s' % path
    result += json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    return result

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def urls_handler(path):
    return 'ST: %s' % path

#if __name__ == "__main__":
#    app.run()


import urls_lib

def generate_page(url, request):
    url_obj = urls_lib.Urls.Parse(url)

generate_page('/', None)
