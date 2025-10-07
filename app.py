from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html",creador="Camacho Zamora Adrian Eduardo")

@app.route('/crearCuenta')
def crear_cuenta():
    return render_template('creacuenta.html')


if __name__ == "__main__":
    app.run(debug=True)