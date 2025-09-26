from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    mensaje = '<h1>Bienvenidos a la calculadora de flask </h1>'
    
    mensaje += '<ol>'
    mensaje += '<li><h2>1.sumar http://127.0.0.1:5000/sumar/10/20</h2></li>'
    mensaje += '<li><h2>2.resta http://127.0.0.1:5000/resta/10/20</h2></li>'
    mensaje += '<li><h2>3.divir http://127.0.0.1:5000/dividir/10/20</h2></li>'
    mensaje += '<li><h2>4.multiplicar http://127.0.0.1:5000/multiplicar/10/20</h2></li>'
    mensaje += '<li><h2>5.maximo http://127.0.0.1:5000/maximo/10/20</h2></li>'
    mensaje += '<li><h2>6.miminimo http://127.0.0.1:5000/minimo/10/20</h2></li>'
    mensaje += '</ol>'
    return mensaje

@app.route('/sumar/<v1>/<v2>')
def sumar(v1, v2):
    s = str(float(v1) + float(v2))
    mensaje = f"<h1>La suma de {v1} + {v2} es {s} </h1>"
    return mensaje

@app.route('/resta/<v1>/<v2>')
def sumar(v1, v2):
    s = str(float(v1) - float(v2))
    mensaje = f"<h1>La resta de {v1} - {v2} es {s} </h1>"
    return mensaje

@app.route('/dividir/<v1>/<v2>')
def sumar(v1, v2):
    s = str(float(v1) / float(v2))
    mensaje = f"<h1>La division de {v1} - {v2} es {s} </h1>"
    return mensaje

@app.route('/multiplicar/<v1>/<v2>')
def sumar(v1, v2):
    s = str(float(v1) * float(v2))
    mensaje = f"<h1>La division de {v1} * {v2} es {s} </h1>"
    return mensaje

if __name__ == '__main__':
    app.run(debug=True)