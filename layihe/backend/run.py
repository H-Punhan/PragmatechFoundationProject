from flask import Flask,render_template,request,redirect

app=Flask(__name__)


@app.route('/')
def write():
    return render_template('index.html')
    
@app.route('/result',methods=['GET','POST'])     
def result():
    if request.method=='POST':
        if request.form['num1']=='' or request.form['num2'] ==' ':
            return redirect('/')
        else:
            return render_template('index.html',result=int(request.form['num1'])+int(request.form['num2']))
    else:
        return redirect('/')
    

if __name__=='__main__':
    app.run(debug=True)

