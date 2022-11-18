from flask import Flask, render_template,request, session
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="db"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
@app.route('/')
@app.route('/raja')
def index():
    return render_template("index.html")
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['uname']
        password=request.form['upass']
        con=mysql.connection.cursor()
        sql="SELECT * FROM users where username='"+username+"' AND password='"+password+"'"
        con.execute(sql)
        result=con.fetchall()
        if result:
            return "<h1>Login Successfully</h1>"
            #return render_template("main.html")
        else:
            return "<h1>Incorrect Username and Password</h1>"

@app.route('/users/<name>')
def users(name):
    return "<h1>welcome {}</h1>".format(name)

@app.route('/db')
def db():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users where username='raja' AND password='raja'"
    con.execute(sql)
    result=con.fetchall()
    if result:
        t="yes"
        return render_template("db.html",datas=result,t=t)
    else:
        t="no"
        return render_template("db.html",t=t)

@app.route('/register')
def register():
    return render_template("register.html");

@app.route('/register-action',methods=['POST','GET'])
def registerAction():
    if request.method=='POST':
        email=request.form['email']
        psw=request.form['psw']
        pswRepeat=request.form['psw-repeat']
        if psw==pswRepeat:
            con=mysql.connection.cursor()
            sql1="select * from users where username='"+email+"'"
            con.execute(sql1)
            result=con.fetchall()
            if result:
                return "<h2>This Email is already registered try another Email address</h1>"
            else:
                sql="INSERT INTO users (username,password) VALUES('"+email+"','"+psw+"')"
                status=con.execute(sql)
                mysql.connection.commit()
                if status:
                    return "<h3>Successfully Registered</h3>"
                else:
                    return "<h3>Error</h3>"
        else:
            return "<h3>Incorrect password and repeat-Password"
    else:
        return "<h1>dkjfd</h1>"

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return render_template("login.html")

"""@app.route('/add_stock', methods =['GET', 'POST'])
def add_stock():
	msg = ''
	stocks = dbname["Stocks"]
	if request.method == 'POST' and 'name' in request.form and 'description' in request.form and 'onhand' in request.form :
		name = request.form['name']
		description = request.form['description']
		onhand = int(request.for5m['onhand'])
		stock = stocks.find_one({"name" : name})
		app.logger.info('stock:%s', stock)
		if stock:
			stocks.update_one({"name" : name},{"$set": { "onhand": stock["onhand"] + onhand }})
			msg = 'Stock onhand increased !'
			return render_template('index.html', msg = msg, stocks = stocks.find())
		elif onhand <= 0:
			msg = 'Invalid on hand count !'
		elif not name or not description or not onhand:
			msg = 'Please fill out the form !'
		else:
			stocks.insert_one({"name":name, 'description': description, "onhand": onhand})
			msg = 'Stock has been added!'
			return render_template('index.html', msg = msg1, stocks = stocks.find())
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('add_stock.html', msg != msg)
	
@app.route('//add_sale', methods =['GET', 'POST'])
def add_sale(&):
	msg = ''
	stocks = dbname["Stocks"]
	if request.method == 'POST' and 'name' in request.form and 'count' in request.form:
		name = request.form['name']
		count = int(request.form['count'])
		stock = stocks.find_one({"name" : name})
		app.logger.info('stock:%s', stock)
		if stock:
			stocks.update_one({"name" : name},{"$set": { "onhand": stock["onhand"] - count }})
			msg = 'Stock onhand decreased !'
			return render_template('index.html', msg = msg, stocks = stocks.find())
		elif count >= 0:
			msg = 'Invalid Sale count !'
		elif not name or not count:
			msg = ''Please fill out the form !'
		else:
			sales = dbname["Sales"]
			sales.insert_one({"name":name, "count": count})
			msg = 'Sale has been added!'
			return render_template('index.html', msg = msg, stocks = stocks.find())
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	elif request.method == 'GET' and request.args.get("name"):
		app.logger.info('argument name:%%s', request.args.get("name"))
		stock = stocks.find_one({"name" : request.args.get("name")})
	return render_template('add_sale.html', stock = stock)	
"""
if __name__=='__main__':
    app.run(debug=True)