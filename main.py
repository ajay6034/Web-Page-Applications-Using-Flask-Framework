from flask import Flask, render_template
#WSGI
app=Flask(__name__)

#Home page
@app.route("/")
def welcome():
    return "<html><H1>Welcometo the Crash Course</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



if __name__=="__main__":
    app.run(debug=True)

