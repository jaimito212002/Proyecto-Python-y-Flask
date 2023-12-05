from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Variables para mensajes
mensaje_acierto = "Acertaste!"  
mensaje_error1 = "El número es menor"
mensaje_error2 = "El número es mayor"


numero_aleatorio = random.randint(1,100)

@app.route('/', methods=['GET'])
def inicio():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def jugar():

  global numero_aleatorio

  intento = request.form['intento']

  if int(intento) == numero_aleatorio:
    resultado = mensaje_acierto
  elif int(intento) < numero_aleatorio:
    resultado = mensaje_error2
    

  else:
    resultado = mensaje_error1
    

  return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
  app.run(debug=True)