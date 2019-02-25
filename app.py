from flask import Flask, render_template, request, flash
from time import time
import pyodbc
import redis
import csv
app = Flask(__name__)
app.secret_key = "Secret"

r = redis.StrictRedis(host='sushma.redis.cache.windows.net', port=6380, db=0, password='fQrhWzt3pQ5QnCBWDzM6GhSQCBCi8p33qLGVexTPn8I=', ssl=True)

connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:sushmak.database.windows.net,1433;Database=quakes;Uid=sushma@sushmak;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
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
    year = request.form['tag2']
    if year == '2010':
        year = 'ten'
    if year == '2011':
        year = 'eleven'
    if year == '2012':
        year = 'twelve'
    if year == '2013':
        year = 'thirteen'
    if year == '2014':
        year = 'fourteen'
    if year == '2015':
        year = 'fifteen'
    if year == '2016':
        year = 'sixteen'
    if year == '2017':
        year = 'seventeen'
    if year == '2018':
        year = 'eighteen'

    if request.method == 'POST':
        query = "SELECT "+ year +" FROM dbo.popul where state = (Select state from dbo.codes where code ="+ "'"+tag1+"')"
        print(query)
        cursor.execute(query)
        r = cursor.fetchall()
        print(r)
    e = time()
    t = e-s
    return render_template('magGreater.html', t=str(t), re=r)

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
