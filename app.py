from flask import Flask, render_template, request, flash
from time import time
import pyodbc
import redis
import csv
app = Flask(__name__)
app.secret_key = "Secret"

r = redis.StrictRedis(host='sushma.redis.cache.windows.net', port=6380, db=0, password='fQrhWzt3pQ5QnCBWDzM6GhSQCBCi8p33qLGVexTPn8I=', ssl=True)

connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:sushmak.database.windows.net,1433;Database=quakes;Uid=sushma@sushmak;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
cursor = connection.cursor()

'''
@app.route('/')
def index():
    start_time = time()
    cursor.execute("CREATE TABLE [dbo].[codes](\
        [code] [nvarchar](8) NULL,\
        [state] [nvarchar](20) NULL)")
    connection.commit()

    query = "INSERT INTO dbo.codes(code,state) VALUES (?,?)"
    

    with open('statecode.csv') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            cursor.execute(query,row)
        connection.commit()
        end_time = time()
        time_taken = (end_time - start_time)
        flash('The Average Time taken to execute the random queries is : ' + "%.4f" % time_taken + " seconds")
        cursor.close()
    return render_template('index.html', t=time_taken)'''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/server', methods=['GET', 'POST'])
def server():
    tag1 = request.form['tag1']
    s = time()
    if request.method == 'POST':
        cursor.execute("SELECT COUNT(*) FROM dbo.county where state ="+ "'"+tag1+"'")
        r = cursor.fetchall()
        re = r[0]

    e = time()
    t = e-s
    return render_template('magGreater.html', t=str(t), re=re)

@app.route('/serverCache', methods=['GET', 'POST'])
def serverCache():
    tag1 = request.form['tag1']
    queryString = "select count(*) from dbo.county where state =" + tag1
    if r.get(queryString) == None:
        s = time()
        cursor.execute(queryString)
        data = cursor.fetchall()
    else:
        s = time()
        data = r.get(queryString)
    e = time()
    t = e - s
    return render_template('magGreater.html', t1=t, re1=data)
