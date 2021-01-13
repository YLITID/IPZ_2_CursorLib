from network import Network
from network import pandasModel
from MainUI import *
import sys
import time
import pandas
import numpy


app = QApplication(sys.argv)

FormLog = QWidget()
uiLog = Ui_Dialog_start_Login()
uiLog.setupUi(FormLog)

FormErr = QWidget()
uiErr = Ui_Dialog_show_error()
uiErr.setupUi(FormErr)

FormChoise = QWidget()
uiChoise = Ui_Dialog_Choise()
uiChoise.setupUi(FormChoise)

FormOrder = QWidget()
uiOrder = Ui_Dialog_Order()
uiOrder.setupUi(FormOrder)


N = Network
status = str(N.connect(N))
if status != '1':
    FormErr.show()

if status == '1':
    FormLog.show()


def timer_Err():
    uiErr.label_Err.setText("Reconnecting")
    status = str(N.reconnect(N))
    print(status)
    if status == '1':
        FormErr.hide()
        FormLog.show()


stErr = uiErr.pushButton_OK.clicked.connect(timer_Err)
print(status)

df = pandas.DataFrame()
dfs = df
dfch = df
def InitChoise():
    global status
    #try:
    status = N.send(N,'c')
    print('Choice status:',status)
    global df, dfs, dfch
    df=N.recv_Obj(N)
    dfch = dfs = df
    model = pandasModel(df)
    uiChoise.tableView.setModel(model)
    uiChoise.tableView.resizeColumnsToContents()
    uiChoise.tableView.resizeRowsToContents()

    arr = df.to_numpy()

    uiChoise.comboBox_Genre.addItem('')
    uiChoise.comboBox_year.addItem('')
    uiChoise.comboBox_vidav.addItem('')
    uiChoise.comboBox_labg.addItem('')
    df_uGenre=df['Genre'].unique()
    df_uYear = df['Year'].unique()
    i=0
    while True:
        if i >= df_uYear.size:
            break
        print(str(df_uYear[i]))
        uiChoise.comboBox_year.addItem(str(df_uYear[i]))
        i+=1

    df_uLang = df['Lang'].unique()
    df_uPubl = df['Publisher'].unique()
    #print(df_unic)
    uiChoise.comboBox_Genre.addItems(df_uGenre)

    uiChoise.comboBox_vidav.addItems(df_uPubl)
    uiChoise.comboBox_labg.addItems(df_uLang)

    #except Exception as e:
    #    print('Error:', e)



Tries = 0
def Login():
    global Tries
    global status
    global adminemode
    adminemode = False
    print(adminemode)
    try:
        status = N.send_R(N,'l',status)
        if status == '-1':
            raise ValueError
        print('Choice status:',status)
        #status = N.send_R('l'.encode(),status).decode()
        if uiLog.lineEdit_user_id.text() == '':
            print('Please enter your login')
            FormErr.resize(200, 80)
            uiErr.label_Err.setText("Please enter your login")
            uiErr.pushButton_OK.hide()
            FormErr.show()
            return
        elif uiLog.lineEdit_password.text() == '':
            print('Please enter your password')
            FormErr.resize(200, 80)
            uiErr.label_Err.setText("Please enter your password")
            uiErr.pushButton_OK.hide()
            FormErr.show()
            return
        elif uiLog.lineEdit_user_id.text() == uiLog.lineEdit_password.text():
            FormErr.resize(300, 80)
            uiErr.label_Err.setText("Username and password shouldn`t be the same")
            uiErr.pushButton_OK.hide()
            FormErr.show()
            print('Username and password shouldn`t be the same')
            return
        else:
            status = N.send_R(N,uiLog.lineEdit_user_id.text(),status)
            if status == '-1':
                raise ValueError
            print('Receiving status: ',status)
            status = N.send_R(N,uiLog.lineEdit_password.text(),status)
            if status == '-1':
                raise ValueError
            print('Login status: ',status)
            if status == '1':
                #Successful login
                pass
            elif status == 'adm':
                #Admin Mode
                pass
            elif status =='2':
                #Unsuccessful login
                if Tries>= 4:
                    uiErr.label_Err.setText('Too many failed attempts')
                    FormErr.resize(200, 80)
                    uiErr.pushButton_OK.hide()
                    FormErr.show()
                    FormLog.hide()
                uiLog.label_success.setText('Unsuccessful login')
                uiLog.label_success.show()
                Tries+=1
                status = str(N.reconnect(N))
            else:
                print('Connection error')
                FormErr.show()



    except Exception as e:
        print('Error:', e)
        FormErr.show()
        return
    if status == 'adm' or '1':
        FormLog.hide()
        FormChoise.show()
        # Successful login
        InitChoise()
def Search():
    global df
    global dfs
    global dfch
    dfs=df
    try:
        if uiChoise.lineEdit_find.text() != '':
            val = uiChoise.lineEdit_find.text()
            dfs = df[(dfch.Name == val) | (dfch.Author_Name ==val)]
        else:
            dfs = df

    except Exception as e:
        print("Error: ",e)
    model = pandasModel(dfs)
    uiChoise.tableView.setModel(model)
    uiChoise.tableView.resizeColumnsToContents()
    uiChoise.tableView.resizeRowsToContents()

def ChangeTable():
    global df
    global dfs
    dfch=dfs
    try:
        if uiChoise.comboBox_Genre.currentText() != '':
            dfch = dfch.loc[df['Genre'] == uiChoise.comboBox_Genre.currentText()]
        if uiChoise.comboBox_year.currentText() != '':
            year = int(uiChoise.comboBox_year.currentText())
            dfch = dfch.loc[dfch['Year'] == year]
        if uiChoise.comboBox_vidav.currentText() != '':
            dfch = dfch.loc[df['Publisher'] == uiChoise.comboBox_vidav.currentText()]
        if uiChoise.comboBox_labg.currentText() != '':
            dfch = dfch.loc[df['Lang'] == uiChoise.comboBox_labg.currentText()]



    except Exception as e:
        print("Error: ", e)
    model = pandasModel(dfch)
    uiChoise.tableView.setModel(model)
    uiChoise.tableView.resizeColumnsToContents()
    uiChoise.tableView.resizeRowsToContents()
index = ''
def toBook():
    global df
    global index
    index = uiChoise.tableView.selectionModel().currentIndex().row()
    print(index)
    FormOrder.show()
    Name = df[df['Book_id']==index]['Name'].iloc[0]
    Author = df[df['Book_id']==index]['Author_Name'].iloc[0]
    Publisher = df[df['Book_id']==index]['Publisher'].iloc[0]
    uiOrder.textBrowser_Details.setText(Name)
    status = N.send(N,'a')

    status = N.send_R(N,str(index), status)

    descr = N.recv(N)
    uiOrder.textBrowser_description.setText(descr)

def Order():
    global index
    status = N.send(N, 'o')

    status = N.send_R(N, str(index), status)

    status = N.recv(N)
    if status == '1':
        uiErr.label_Err.setText('Success')
        uiErr.pushButton_OK.hide()
        FormErr.setWindowTitle("Info")
        FormErr.show()
    else:
        FormErr.show()

res = uiChoise.pushButton_Choise.clicked.connect(ChangeTable)
res = uiChoise.pushButton_Search.clicked.connect(Search)
res = uiLog.pushButton_Login.clicked.connect(Login)
res = uiChoise.pushButton_toBook.clicked.connect(toBook)
res = uiOrder.pushButton_order.clicked.connect(Order)
print(res)


#uiChoise.comboBox_labg.activated[str].connect(onChanged)
#uiChoise.comboBox_vidav.activated[str].connect(onChanged)
#uiChoise.comboBox_year.activated[str].connect(onChanged)
#uiChoise.comboBox_Genre.activated[str].connect(onChanged)

#main()
if __name__ == '__main__':
    sys.exit(app.exec_())