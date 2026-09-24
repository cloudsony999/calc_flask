from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/callme')
def operation():
    n1=int(request.args.get('num1'))
    n2=int(request.args.get('num2'))
    sum=n1+n2
    # return "<body bgcolor='green' text='yellow'><h1>the sum is {}</h1>" \
    #        "</body>".format(sum)       

    html='''
    <body style="margin:0; padding:0; background:linear-gradient(135deg, #667eea, #764ba2); font-family:Arial, sans-serif;">
    
    <div style="width:400px; margin:80px auto; background:white; padding:35px; border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.3);">
    <h1>the sum is {}</h1>
    </div>
    </div>
    </body>
    '''.format(sum)
    return html



if __name__=='__main__':
    app.run(debug=True)


