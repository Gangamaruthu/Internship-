from flask import Flask , render_template, request,redirect, url_for
import pymysql
app = Flask (__name__)
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="signup"
)
cursor = conn.cursor()
@app.route('/')
def home():
    return render_template('signup.html')

    
@app.route('/create' , methods=['GET','POST'])
def create():
    msg=''
    output=""
    if request.method =='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        mail_id = request.form['mail_id']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        print(firstname,lastname)
        
        if password != confirm_password:
            return render_template('signup.html', msg="Password mismatch")
        print( "Password Match")
        
        cursor = conn.cursor()
       
        sql= """INSERT INTO login (firstname,lastname,mail_id, password,confirm_password) values(%s,%s,%s,%s,%s)"""
        val = (firstname,lastname,mail_id , password,confirm_password )
        cursor.execute(sql,val)
        conn.commit()

#ithula kudukura html page vara page ku poova ithula ulla return render_template la kudupom 

    return render_template('loginpage.html')


@app.route('/home')
def log():
    return render_template('home.html')

@app.route('/new', methods=['GET','POST'])
def new():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        
        sql= """INSERT INTO register(username,password) values(%s,%s)"""
        val =( username , password)
        cursor.execute(sql,val)
        conn.commit()
        
    return render_template('home.html')


@app.route('/logo')
def logo():
    return render_template('mainpage.html')

@app.route('/lipstick1')
def lipstick1():
    return render_template('lipstick1.html')

@app.route('/lipstick2')
def lipstick2():
    return render_template('lipstick2.html')

@app.route('/lipstick3')
def lipstick3():
    return render_template('lipstick3.html')

@app.route('/lipstick4')
def lipstick4():
    return render_template('lipstick4.html')

@app.route('/sunscreen1')
def sunscreen1():
    return render_template('sunscreen1.html')

@app.route('/sunscreen2')
def sunscreen2():
    return render_template('sunscreen2.html')

@app.route('/sunscreen3')
def sunscreen3():
    return render_template('sunscreen3.html')

@app.route('/sunscreen4')
def sunscreen4():
    return render_template('sunscreen4.html')

@app.route('/hairserum1')
def hairserum1():
    return render_template('doveserum.html')

@app.route('/hairserum2')
def hairserum2():
    return render_template('tershairserum.html')

@app.route('/hairserum3')
def hairserum3():
    return render_template('hairserum3.html')

@app.route('/hairserum4')
def hairserum4():
    return render_template('hairserum4.html')

@app.route('/eyelinear1')
def eyelinear1():
    return render_template('eyelinear1.html')


@app.route('/eyelinear2')
def eyelinear2():
    return render_template('eyelinear2.html')

@app.route('/eyelinear3')
def eyelinear3():
    return render_template('eyelinear3.html')


@app.route('/eyelinear4')
def eyelinear4():
    return render_template('eyelinear4.html')

@app.route('/bodywash1')
def bodywash1():
    return render_template('bodywash1.html')

@app.route('/bodywash2')
def bodywash2():
    return render_template('bodywash2.html')

@app.route('/bodywash3')
def bodywash3():
    return render_template('bodywash3.html')

@app.route('/bodywash4')
def bodywash4():
    return render_template('bodywash4.html')

if __name__ == "__main__":
    app.run (debug=True ,port=5000)