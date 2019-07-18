from flask import Flask, render_template, request
#New line for Experiment branch


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello , World !'

@app.route('/carform', methods=['GET'])
def form1():
    return render_template('test1.html')

@app.route('/form_submitted', methods=['POST'])
def form2():
    print request.form
    print request.args
    return "Car I Selected is %s" %(request.form.get('cars'))



if __name__ == "__main__":
    app.run()