from flask import Flask, render_template

app = Flask(__name__)

#Routes

@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/grado/<int:celsius>")
def grado(celsius):
    return render_template("grado.html", resultado = celsius * 9/5 + 32)

@app.route("/prestamo/<int:monto>")
def prestamo(monto):
    return render_template("prestamo.html", cuota = monto * ((0.01897 * ((1 + 0.01897) ** 12)) / (((1 + 0.01897) ** 12) - 1)))


if __name__ == "__main__":
    app.run(debug=True)