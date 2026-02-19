from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def home():
    return '''

    <h1> Aplicación Calculadora </h1>

    <p> Opciones disponibles: </p>

    <ul>
        <li>
             <a href="/suma?a=8&b=12"> 
             Suma 
             </a>
        </li>
        <li> 
            <a href="/resta?num1=12&num2=4"> 
            Resta
            </a>
        </li>
        <li>
            <a href="/multiplicacion?a=5&b=9"> 
            Multiplicación
            </a>
        </li>
        <li> <a href="/division?c=20&d=5"> 
        División 
        </a> 
        </li>

        </li>
        <li> <a href="/divisionPiso?e=7&f=2"> 
        División Piso 
        </a> 
        </li>
        </li>
        <li> <a href="/numeroAleatorio?min=1&max=10"> 
        Número Aleatorio
        </a> 
        </li>
    </ul>


    '''



#Esta es una ruta adicional en la aplicación, que se activa cuando el usuario accede a la URL "/suma".
@app.route('/suma')
def ruta_suma(): 
    a=request.args.get("a", type=float) #Aquí se obtiene el valor del parámetro "a" de la URL, y se convierte a un número flotante. Si el parámetro no está presente, se asigna el valor None.
    b=request.args.get("b", type=float) 
    resultado = a + b
    return f'''
    "La suma de los numeros {a} y {b} es: {resultado} "  
'''
@app.route('/resta')
def ruta_resta():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)
    resultado = num1 - num2
    return f"La resta de los numeros {num1} y {num2} es: {resultado} "


@app.route('/multiplicacion')
def ruta_multiplicacion():
    a=request.args.get("a", type=float)
    b=request.args.get("b", type=float)
    resultado = a * b
    return f'''
    "La multiplicación de los numeros {a} y {b} es: {resultado} "
    <a href="/"> Volver al inicio </a>
'''

@app.route('/division')
def ruta_division():
    c=request.args.get("c", type=float)
    d=request.args.get("d", type=float)
    resultado = c / d
    return f'''
    "La división de los numeros {c} y {d} es: {resultado} "
    <a href="/"> Volver al inicio </a>
'''

@app.route('/divisionPiso')
def ruta_divisionPiso():
    e=request.args.get("e", type=float)
    f=request.args.get("f", type=float)
    resultado = e // f
    return f'''
    "La división piso de los numeros {e} y {f} es: {resultado} "
    <a href="/"> Volver al inicio </a>
'''

@app.route('/numeroAleatorio')
def ruta_numeroAleatorio():
    import random
    min=request.args.get("min", type=int)
    max=request.args.get("max", type=int)
    resultado = random.randint(min, max)
    return f'''
    "El número aleatorio generado entre {min} y {max} es: {resultado} "
    <a href="/"> Volver al inicio </a>
'''




    



#Esto me permite actualizar rapidamente los cambios sin tener que reiniciar el servidor cada vez
    if __name__ == "__main__":
        app.run(debug=True)
