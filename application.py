from flask import Flask, render_template, url_for
application = Flask(__name__)

# application.config['SECRET_KEY'] = 'A89Xb9_2#fPpsko'
# app.config['SERVER_NAME'] = 'localhost:5000'
# app.config.from_pyfile('config.cfg')

@application.route('/')
def profile():
	return render_template("profile.html")
  
  
@application.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")
	
@application.route('/unlock')
def unlock():
	return render_template("unlock.html")
	
@application.route('/upload')
def upload():
	return render_template("upload.html")
	
@application.route('/account')
def account():
	return render_template("account.html")
		
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
