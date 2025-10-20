from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_y_dificil_de_adivinar'

@app.route("/")
def sesion():
    return render_template("sesion.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route('/animalesexoticos')
def animales():
    return render_template('animales.html')

@app.route('/vehiculosantiguos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillasdelmundo')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acercade')
def acerca():
    return render_template('acerca.html')

@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/registrame', methods= ("GET", "POST"))
def registro():
    error = None
    if request.method == "POST":
        nombreCompleto = request.form["nombreCompleto"]
        fecha = request.form["fecha"]
        genero = request.form["genero"]
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]
        
    if error != None:
        flash(error)
        return render_template("crear.html")
    else:
        flash(f"Tu cuenta se a creado {nombreCompleto}")
        return render_template("inicio.html")


if __name__ == "__main__":
    app.run(debug=True)