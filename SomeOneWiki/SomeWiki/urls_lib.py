'''
Created on 30 сент. 2013 г.

@author: garet
'''
import hashlib


import yaml

from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import unquote
from urllib.parse import quote

class UrlCacher:
    @staticmethod
    def Parse(url):
        result = {}
        url_tmp = unquote(url)
        url_obj = urlparse(url_tmp)
        if len(url_obj.path) > 0 and url_obj.path[0] == '/':
            path = url_obj.path[1:]
        else:
            path = url_obj.path
        splited_url = path.split('/')
        if len(splited_url) > 0 and splited_url[-1] == '':
            result['section'] = path
            result['aliase'] = ''
        else:
            section_list = splited_url[:-1]
            result['section'] = UrlCacher.SectionsMerge(section_list)
            result['aliase'] = splited_url[-1]
        result['params'] = parse_qs(url_obj.query)
        return result
    
    @staticmethod
    def SectionsMerge(lstlst, sep='/'):
        all = ''
        for lst in lstlst:
            all += lst + sep
        return all
    
    _schemes = {}
    _urls = {}
    def Get(self, url):
        if url in self._urls:
            return self._urls[url]
        return None
    
    def Add(self, url, scheme_1, scheme_2):
        if url not in self._urls:
            self._urls[url] = {}
            self._urls[url]['scheme_1'] = self.CacheScheme(scheme_1)
            self._urls[url]['scheme_2'] = self.CacheScheme(scheme_2)
        return
    
    def CacheScheme(self, scheme):
        scheme_data = scheme.encode('utf-8')
        scheme_hash = hashlib.md5(scheme_data).hexdigest()
        if scheme_hash not in self._schemes:
            self._schemes[scheme_hash] = scheme
            return scheme_hash
        return scheme_hash

    def __init__(self):
        scheme_1 = [
                         {
                              'position':'top',
                              'index':0,
                              'module':'wiki_article',
                              'template':'default',
                         },
                    ]
        scheme_2 = [
                         {
                              'position':'top',
                              'index':0,
                              'module':'wiki_article',
                              'template':'default',
                         },
                    ]
        scheme_yaml_1 = yaml.dump(scheme_1)
        self.Add('/', scheme_yaml_1, scheme_yaml_1)
        scheme_yaml_2 = yaml.dump(scheme_2)
        self.Add('/index.php', scheme_yaml_2, scheme_yaml_2)

"""
url = quote('%7Eguido/Python.html/fd sdf/,?asd=1&p=0&param=[ываавы,gdfgf]')
obj = UrlCacher.Parse(url)

cacher = UrlCacher()
print(cacher._urls)
"""