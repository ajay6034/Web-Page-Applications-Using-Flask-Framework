## Building URl Dynamically
# Variable Rule
## Jinja 2 Template Engine: Have multiple ways 
# to read data source from backend in html


#WAYS

'''
1. {{ }} expressions to print output in html
2. {%...%} conditions, for loops
3. {#...#} this is for comments

'''




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
@app.route('/sucess/<int:score>')
def sucess(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    
    return render_template('result.html',results=res)



## variable rule
@app.route('/sucessres/<int:score>')
def sucessres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,"res":res}
    
    return render_template('result1.html',results=exp)



@app.route('/sucessif/<int:score>')
def sucessif(score):
    
    return render_template('result.html',results=score)


if __name__=="__main__":
    app.run(debug=True)

