import pyodbc as sql
import pandas as pd


class DataBase(object):
    admin_st=''
    def start_conn(self):
        cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost;"
            "Database=CursorDC;"
            "Trusted_Connection=yes;")
        try:
            self.cnxn = sql.connect(cnxn_str)
        except Exception as e:
            self.Error(e)
        cursor = self.cnxn.cursor()
        self.start_check(self)
    def start_check(self):
        try:
            self.cursor = self.cnxn.cursor()
        except Exception as e:
            self.Error(self,e)
        print(pd.read_sql("SELECT * FROM Login", self.cnxn))

    def SearchLog(self, login, password):
        print(login, password)
        try:df = pd.read_sql("SELECT L.admin_st,L.login,P.password FROM Login as L "
                             "INNER JOIN Login_p as P on L.User_id = P.User_id ", self.cnxn)
        except Exception as e:
            self.Error(self,e)

        print(df)
        self.login = login
        reslog = False
        try:
            passcheck = df[df['login'] == login]['password'].iloc[0]
            if passcheck == password:
                reslog = True
                self.admin_st = int(df[df['login'] == login]['admin_st'].iloc[0])
                if self.admin_st == 1:
                    reslog = 'adm'
            print("Result: ", reslog,'\nPass: ', passcheck,'\nAdmin Mode:', self.admin_st)
            return reslog
        except:
            return reslog
    def ShowChoiseDef(self):
        try:
            df = pd.read_sql("SELECT * FROM FLIGHTS", self.cnxn)
            return df
        except Exception as e:
            self.Error(self, e)
            return -1
    def ShowDescr(self, index):
        try:

            sql_text="SELECT Descr from Descr WHERE Book_id = {index}".format(index=index)

            data = pd.read_sql(sql_text,self.cnxn)
            descr = data['Descr'].iloc[0]

            return descr
        except Exception as e:
            self.Error(e)
            return -1

    def Order(self, index):
        try:
            login = self.login

            self.cursor.execute(f"INSERT INTO Orders (Login,Book_id) values('{login}',{index})")
            self.cnxn.commit()
            return '1'
        except Exception as e:
            self.Error(e)
            return '-1'
    def Error(self,e):
        print("Error in database: ", e)