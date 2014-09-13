#importing the Person class and flask
from Person import *
from flask import Flask

app = Flask(__name__)

#want it to redirect to the login screen if they are not logged in
#or the main screen if they are logged in
@app.route('/')
def Redirect(): pass

#login screen using CAS to login w/ a rpi email
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login() #havent made this

#Profile page, should be able to edit user data (name/summoner name)
@app.route('/user/<username>')
def profile(username): pass

#main page where people can see other other's data 
@app.route('/main')


#just a bit of testing around
with app.test_request_context():
    print url_for('login')

#repository
#https://github.com/tkxxrf/Summonersplatform.git


if __name__ == '__main__':
    #app.run(host='0.0.0.0') for other people to see
    app.run()


