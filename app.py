from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

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


if __name__ == "__main__":
    app.run(debug=True)