"""
views imports app, auth, and models, but none of these import views
"""

from flask import render_template # ...etc , redirect, request, url_for
from app import app
from auth import auth
from models import User

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)


from controller import getData
@app.route("/data")
def web_getData():
    return getData('https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314','records')


from flask import redirect, url_for, request
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

# @app.route('/private/')
# @auth.login_required
# def private_view():
#     # ...
#     user = auth.get_logged_in_user()
#     return render_tempate(...)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True) # default port:5000




