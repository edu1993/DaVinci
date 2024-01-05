from pickle import TRUE
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/nosotros')

def nosotros():
    return render_template('nosotros.html')

@app.route('/mat', methods=['GET', 'POST'])
def mat():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            suma = num1 + num2
            return render_template('mat.html', suma=suma)
        except ValueError:
            error_message = 'Por favor, ingrese números válidos.'
            return render_template('mat.html', error_message=error_message)
    return render_template('mat.html')

@app.route('/collazt',methods=['GET','POST'])
def collazt():
    numeros = list()
    if request.method == 'POST':
        i=int(request.form['num'])
        while i != 1:
            if i%2==0:
                i/=2
            else:
                i=3*i+1
            numeros.append(int(i))
    return render_template('collazt.html',numeros=numeros)

if __name__ == '__main__':
    app.run(debug=TRUE)
