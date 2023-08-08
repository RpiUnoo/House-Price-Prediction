from flask import Flask,render_template,redirect,request,send_file
import stand_alone

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        
        area = float(request.form['area'])
        bhk = int(request.form['uiBHK'])
        bath = int(request.form['uiBathrooms'])
        location = str(request.form['iloc'])

        price = stand_alone.pred_score(location,area,bath,bhk)

    return render_template('index.html',your_price=price)


if __name__=='__main__':
    app.run(debug=True)