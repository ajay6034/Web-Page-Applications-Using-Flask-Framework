from flask import Flask, render_template,request
#WSGI
app=Flask(__name__)

#Home page
@app.route("/")
def welcome():
    return "<html><H1>Welcometo the Crash Course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name= request.form['name']
        email= request.form['email']
        message=request.form['message']
        return f'Hi {name} {message} your mailid is: {email}'
        
    return render_template('form.html')

## variable rule
@app.route('/sucess/<score>')
def sucess(score):
    return 'The marks you got is '+ score

if __name__=="__main__":
    app.run(debug=True)

