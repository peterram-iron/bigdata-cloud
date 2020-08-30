from flask import Flask, render_template, request
from ml_model import spam_classifier

app = Flask(__name__)
@app.route('/', methods = ['POST','GET'])

def run_model():

    if request.method == 'POST':
        input_string = request.form['name']

        # write here the code that calls the spam_classifier function and stores the result in a variable called "result"
        
        # In the return statement add a variable that you will pass to the html in order to visualize the results
        return render_template('main.html')

    else: 
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')