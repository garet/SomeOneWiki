'''
Created on 25 сент. 2013 г.

@author: garet
'''
import json

from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import unquote
from urllib.parse import quote

from flask import Flask
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template

class SomeClass:
    def Apt(self):
        return 'Say Hello!'

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
    data1 = SomeClass()
    data2 = {'apt': 1, 'center': 'Center Text!'}
    return render_template('/pages/default/index.tpl', data1=data1, data2=data2)


if __name__ == "__main__":
    app.debug = True
    app.run()


"""
from SomeWiki.urls_lib import UrlCacher

def generate_page(url, request):
    url_obj = UrlCacher.Parse(url)
    print(url_obj)

generate_page('/asjdjkasdjkasd/asd/as?d=/asd/asd/ads.php', None)
"""