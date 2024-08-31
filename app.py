from flask import Flask
#WSGI
app=Flask(__name__)

#Home page
@app.route("/")
def welcome():
    return "Welcome To The Data Scinec"

if __name__=="__main__":
    app.run(debug=True)

