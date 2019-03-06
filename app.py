from flask import Flask, render_template, request, flash
from time import time
import pyodbc
import redis
from sqlalchemy import create_engine
import urllib
import csv
app = Flask(__name__)
app.secret_key = "Secret"

#r = redis.StrictRedis(host='sushma.redis.cache.windows.net', port=6380, db=0, password='fQrhWzt3pQ5QnCBWDzM6GhSQCBCi8p33qLGVexTPn8I=', ssl=True)

params = urllib.parse.quote_plus("Driver={ODBC Driver 13 for SQL Server};Server=tcp:sushmak.database.windows.net,1433;Database=quakes;Uid=sushma@sushmak;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

#connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:sushmak.database.windows.net,1433;Database=quakes;Uid=sushma@sushmak;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#cursor = connection.cursor()
'''
@app.route('/')
def index():
    start_time = time()
    cursor.execute("CREATE TABLE [dbo].[education](\
        [entity] [nvarchar](40) NULL,\
        [code] [nvarchar](8) NULL,\
        [yr] int NULL,\
        [blpercent] float NULL)")
    connection.commit()

    query = "INSERT INTO dbo.education(entity,code,yr,blpercent) VALUES (?,?,?,?)"
    

    with open('educationshare.csv') as csvfile:
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
    return render_template('index.html', t=time_taken)
'''

@app.route('/')
def index():
    return render_template('index.html')
'''
@app.route('/barchart', methods=['POST'])
def bar():
    if request.form['form'] == 'ShowGraph':
        mag1 = request.form['vmag1']
        mag2 = request.form['vmag2']
        rows = engine.execute("select CAST(locationsource as varchar(max)) as locationsource,count(*) as cnt from quake where mag between "+mag1+" and "+mag2+" group by CAST(locationsource as varchar(max));").fetchall()
        #rows = engine.execute("select top(1000) id, latitude, longitude, mag, CAST(locationsource as varchar(max)) as locationsource from earthquake2;").fetchall()
        rows = [dict(row) for row in rows]
        #return render_template('visual.html', a=rows, chartType='Scatter')
        #return render_template('visual.html', a=rows, chartType='Pie')
        return render_template('display.html', a=rows, chartType='Bar')
'''

@app.route('/qstn6', methods=['GET', 'POST'])
def qstn6():
    tag1 = request.form['yr1']
    tag2 = request.form['r1']
    tag3 = request.form['r2']
    tag4 = request.form['r3']
    tag5 = request.form['r4']
    tag6 = request.form['r5']
    tag7 = request.form['r6']
    if tag1 == '2010':
        tag1 = 'ten'
    if tag1 == '2011':
        tag1 = 'eleven'
    if tag1 == '2012':
        tag1 = 'twelve'
    if tag1 == '2013':
        tag1 = 'thirteen'
    if tag1 == '2014':
        tag1 = 'fourteen'
    if tag1 == '2015':
        tag1 = 'fifteen'
    if tag1 == '2016':
        tag1 = 'sixteen'
    if tag1 == '2017':
        tag1 = 'seventeen'
    if tag1 == '2018':
        tag1 = 'eighteen'

    query = "select sum(case when " + tag1 + " <= " + "'" + tag2 + "'" + " and "+ tag1 + " >=" + "'" +tag3 +"'" + " then 1 else 0 end) as states1, sum(case when " + tag1 + " > " + "'" + tag4 + "'" + " and " + tag1 + " <= " + "'" +tag5+"'" + "then 1 else 0 end) as states2, sum(case when " + tag1 + " > " +"'" +tag6+"'"+" and " + tag1 + " <= " +"'" + tag7 + "'" + " then 1 else 0 end) as states3 from popul"
    if request.method == 'POST':
        print(query)
        s = time()
        r = engine.execute(query).fetchall()
        print(r)
    e = time()
    t = e-s
    return render_template('magGreater.html', data1=r, t1=t)


'''
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

@app.route('/qstn8', methods=['GET', 'POST'])
def qstn8():
    tag1 = request.form['tag8']
    query = "select county from dbo.county where state =(Select state from codes where code ="+"'"+tag1+"')"
    if request.method == 'POST':
        print(query)
        #s = time()
        cursor.execute(query)
        r = cursor.fetchall()
        print(r)
    #e = time()
    #t = e-s
    #return render_template('magGreater.html', data=r, t=t)

@app.route('/qstn9', methods=['GET', 'POST'])
def qstn9():
    tag1 = request.form['tag1']
    tag2 = request.form['tag2']
    year = request.form['y']
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
    s = time()

    query = "select state from popul where "+year+" BETWEEN " +"'"+tag1+"'"+ " AND " + "'"+tag2+"'"
    if request.method == 'POST':
        print(query)
        cursor.execute(query)
        r = cursor.fetchall()
        print(r)
    e = time()
    t = e-s
    return render_template('magGreater.html', data1=r, t1=t)


@app.route('/qstn10', methods=['GET', 'POST'])
def qstn10():
    tag1 = request.form['tag10']
    s = time()
    for i in range(tag1):
        qstn8()
        qstn9()
    e = time()
    t = e-s
    return render_template('magGreater.html', t=t)

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
'''