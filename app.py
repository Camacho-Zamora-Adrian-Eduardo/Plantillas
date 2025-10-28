from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_y_dificil_de_adivinar'

USUARIOS_REGISTRADOS = {
    "adrian@cetis.edu.mx": {"nombre": "Adrian Camacho", "password": "Cetis61"}
}

@app.route("/")
def index():
    return render_template("inicio.html")


@app.route("/inicioDeSesion")
def inisioSesion():
    return render_template("sesion.html")

@app.route('/validaSesion', methods=['GET','POST'])
def validasesion():
    
    if request.method == "POST":
        email = request.form.get('email','').strip()
        password = request.form.get('password','')
        # Validad credenciales
        if not email or not password:
            flash('Por favor ingresa email y contraseña','error')
        elif email in USUARIOS_REGISTRADOS:
            usuario = USUARIOS_REGISTRADOS[email]
            if usuario['password'] == password:
                # Credenciales correctas
                session['usuario_email'] = email
                session['usuario'] = usuario['nombre']
                session['logueado'] = True
                
                return redirect(url_for('inicio'))
            else:
                flash('Contraseña incorrecta','error')
        else:
            flash('Usuario no encontrado','error')
            
            return render_template('sesion.html')
        


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
        password = request.form["contraseña"]
        
    if error != None:
        flash(error)
        return render_template("crear.html")
    else:
        flash(f"Tu cuenta se a creado {nombreCompleto}")
        return render_template("inicio.html")


if __name__ == "__main__":
    app.run(debug=True)