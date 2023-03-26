from flask import Flask, request , render_template , jsonify


app = Flask(__name__)

@app.route('/') 
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    if (request.method == 'POST'):
        OPS = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']
        if ops == 'add':
            r = num1+num2
            result = "The sum of " +str(num1) +'and' + str(num20) + "is" + str(r) 

        return render_template('results.html' , result = result)
    
if __name__=="__main__":
   app.run(host = "0.0.0.0")
            