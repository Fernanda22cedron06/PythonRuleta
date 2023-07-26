from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('casino.html')

if __name__ == '__main__':
    app.run(debug=True)

def ruleta():
    opciones = [i for i in range(37)]
    colores = ['rojo' if(i > 0 and i % 2==1) else 'negro' if (i % 2 == 0) else 'verde' for i in opciones]
    resultado = random.choice(opciones)
    color = colores[resultado]
    return resultado, color
print("Bienvenido a la ruleta")
input("presione enter para comenzar")

resultado, color = ruleta()
print(f"el resultado es {resultado} ,{color}")