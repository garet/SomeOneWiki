'''
Created on 23 sept. 2013 г.

@author: garet
'''


from SomeWiki.Sql import *

class ArticleModel:
    def __init__(self, conn, cursor, type_db, pref = ''):
        self.db = SqlBuilder(conn, cursor, type_db, pref, debug = True)
        
    def Add(self, page_id, index, text, user_id = None, user_ip = None):
        #self.db.Insert('', values)
        return
    
    def AddRevision(self, article_id, text, user_id = None, user_ip = None):
        cur_rev = self.db.Select()\
                         .From('{pref}texts')\
                         .Where('text_article_id = %s', article_id)\
                         .OrderBy('text_revision DESC')\
                         .Execute()\
                         .FetchOne()
        if len(cur_rev) == 0:
            revision = 0
        else:
            revision = cur_rev['text_revision'] + 1
        # Prepare parameters
        values = {'text_article_id': article_id,
                  'text_revision': revision,
                  'text_source': 0,
                  'text_result': 0,
                  'text_user_id': user_id,
                  'text_user_ip': user_ip,}
        self.db.Insert('{pref}texts', values).Execute()
        self.db.Commit()
        print(cur_rev)

import psycopg2
import psycopg2.extras

connection = psycopg2.connect(database="SomeWiki", user="garet", password="joker12")
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

obj = ArticleModel(connection, cursor, 'pg', 'tbl_')
obj.NewRevision(0, 'text', 0, 0)