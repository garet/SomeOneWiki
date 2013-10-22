'''
Created on 15 авг. 2013 г.

@author: garet
'''

class SqlBuilder1:
    def SelectSql(self, table, columns, where, limit=None, offset=None):
        cols = '*'
        if columns != '*' and columns != None:
            cols = ''
            for column in columns:
                cols += column + ','
            cols = cols.strip(',')
        limit_str = ''
        if limit != None and offset != None:
            limit_str += ' LIMIT {0},{1}'.format(limit, offset)
        elif offset == None and limit != None:
            limit_str += ' LIMIT {0}'.format(limit)
        if where != '' and where != None:
            sql = 'SELECT {0} FROM {1} WHERE {2}{3};'
            return sql.format(cols, table, where, limit_str)
        else:
            sql = 'SELECT {0} FROM {1}{2};'
            return sql.format(cols, table, limit_str)
        

class SqlConstruct:
    sql = ''
    debug = True
    __params_stack = {}
    __count_params = 0
    
    def __init__(self, pref = '', debug = True):
        self.pref = pref
        self.debug = debug
        
    def Select(self, table, columns):
        cols = '*'
        if type(columns) is list or type(columns) is tuple:
            cols = ''
            for column in columns: 
                cols += column + ','
            cols = cols.strip(',')
        self.sql += 'SELECT {0} FROM {1} \r'.format(cols, table)
        return self
    
    def Where(self, value):
        self.sql += 'WHERE {0} \r'.format(value)
        return self
    
    def Limit(self, limit, offset = None):
        if offset != None:
            self.sql += 'LIMIT {0},{1} '.format(limit, offset)
        else:
            self.sql += 'LIMIT {0} '.format(limit)
        return self
    
    def InnerJoin(self, table, condt):
        self.sql += 'INNER JOIN {0} ON {1} \r'.format(table, condt)
        return self
    
    def LeftJoin(self, table, condt):
        self.sql += 'LEFT JOIN {0} ON {1} \r'.format(table, condt)
        return self
    
    def RightJoin(self, table, condt):
        self.sql += 'RIGHT JOIN {0} ON {1} \r'.format(table, condt)
        return self
    
    def FullJoin(self, table, condt):
        self.sql += 'FULL JOIN {0} ON {1} \r'.format(table, condt)
        return self
    
    def Insert(self, table, items):
        columns = ''
        values = ''
        for item in items: 
            columns += item + ','
            values += '$' + str(self.__count_params) + ','
            self.__count_params += 1
            self.__params_stack.update(items)
        #print(self.__params_stack)
        columns = columns.strip(',')
        values = values.strip(',')
        tmp = 'INSERT INTO {0}({1}) VALUES ({2}) \r'
        self.sql += tmp.format(table, columns, values)
        return self
    
    def InsertMany(self, table, items):
        return self
    
    def Update(self, table, items):
        values = ''
        for item in items: 
            values += '{0}=${1},'.format(item, self.__count_params)
            self.__count_params += 1
        values = values.strip(',')
        tmp = 'UPDATE {0} SET {1} \r'
        self.sql += tmp.format(table, values)
        return self
    
    def Delete(self, table):
        self.sql += 'DELETE FROM {0} \r'.format(table)
        return self
    
    def Run(self, params = None):
        result = self.sql.replace('{pref}', self.pref)
        if params != None:
            result = result.format(params)
        result = result.strip() + ';\r\r'
        if self.debug == True:
            print(result)
        return result
    
    def Clear(self):
        self.sql = ''
        self.__count_params = 0
        return self



params = {' user_name':'garet', 'user_password':'sdasdasd23dfasdf'}
obj = SqlConstruct('tpl_')
obj.Select('{pref}users', ['id','name','score'])\
   .InnerJoin('{pref}posts', '{pref}users.user_id={pref}posts.post_user_id')\
   .Where('user_name={0} AND user_password={1}')\
   .Run()

obj.Clear()
items = {'user_id':1, 'user_names':'garet'}
obj.Insert('{pref}users', items).Run()

obj.Clear()
items = {'user_id':1, 'user_names':'garet'}
obj.Update('{pref}users', items)\
   .Where('user_name={0}')\
   .Run()

obj.Clear()
items = {'user_id':1, 'user_names':'garet'}
obj.Delete('{pref}users')\
   .Where('user_name={0}')\
   .Run()
   
items = [{'name':'garet',},{'name':'garet',},]
print(type(items))
items = ({'name':'garet',},{'name':'garet',},)
print(type(items))



