from flask import Flask, render_template, request,redirect, url_for
#from flaskext.mysql import MySQL
app = Flask(__name__)

#mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'vasu19@@'
#database added
app.config['MYSQL_DATABASE_DB'] = 'firstdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)


#demo
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        # #cur = mysql.get_db().cursor()
        # cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        # mysql.get_db().commit()
        # cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')
@app.route('/logout.html/')
def logout():
    return render_template('logout.html')
if __name__=='__main__':
    app.run(debug=True
            )
