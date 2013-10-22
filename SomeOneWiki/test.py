'''
Created on 29 авг. 2013 г.

@author: garet
'''
"""
# BUG
# Some fix: https://bugs.launchpad.net/ubuntu/+source/py-postgresql/+bug/1182835
# /usr/lib/python3/dist-packages/postgresql/types/io/__init__.py
# Line:  return __import__(__name__ + '.' + relmod, fromlist = True)#, level = 1)
import postgresql
db = postgresql.open('pq://garet:joker12@localhost:5432/SomeWiki')
#db.execute("CREATE TABLE emp (emp_first_name text, emp_last_name text, emp_salary numeric)")
#make_emp = db.prepare("INSERT INTO emp VALUES ($1, $2, $3)")
#make_emp("John", "Doe", "75.322")
#with db.xact():
#    make_emp("Jane", "Doe", "75.322")
#    make_emp("Edward", "Johnson", "82.744")

sql_obj = db.prepare("INSERT INTO emp VALUES ($1, $2, $3)")
"""
import pymorphy2
import urllib.request
import lxml.html



def GetPage(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return data.decode('utf-8')

def GetData(text):
    page = lxml.html.document_fromstring(text)
    #title = page.xpath('//td[@class="text"]')
    p = page.xpath('//td[@class="text"] //p')
    text = ''
    for i in range(0, len(p)):
        text += p[i].text + ' \r'
    return text

def GetWords(text):
    alphabet = 'ёйцукенгшщзхъфывапролджэячсмитьбю '
    text = text.lower()
    tmp = ""
    for letter in text:
        if letter in alphabet:
            tmp += letter
        elif letter == '\r':
            tmp += ' '
    tmp = tmp.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
    result_list = []
    for item in tmp.split(' '):
        if len(item) > 3:
            result_list.append(item)
    return result_list

def Normalise(morph, word):
    #morph = pymorphy2.MorphAnalyzer()
    obj = morph.parse(word)[0]
    return obj.lexeme


url = 'http://referats.yandex.ru/all.xml?mix=all'
text = ''
for i in range(0, 3):
    data = GetPage(url)
    text += GetData(data)

with open("text_out", "w") as f2:
    f2.write(text)



morph = pymorphy2.MorphAnalyzer()

p = morph.parse('dogs')
print(p)

word_list = GetWords(text)
result_list = {}
for i in range(0, len(word_list) - 2):
    word1 = Normalise(morph, word_list[i])
    word2 = Normalise(morph, word_list[i + 1])
    word_line = word1[0][0] + ' ' + word2[0][0]
    if word_line in result_list.keys():
        result_list[word_line] += 1
    else:
        result_list[word_line] = 0
    if i % 10 == 0:
        print(i)
        
sorted_x = sorted(result_list.items(), key=lambda x: x[1])
#print(result_list)
#print(sorted_x)

with open("text2", "w") as f2:
    for key in sorted_x:
        f2.write('{0}\r'.format(key))
