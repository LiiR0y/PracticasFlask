from flask import Flask, render_template
from clientes import datos

app = Flask(__name__)

#Routes

@app.route('/')
def Index():
    title = "Bienvenido Al Sitio Web"
    return render_template("index.html", title = title )

@app.route('/clientes')
def Clientes():
    title = "Detalles de Clientes"
    clientes = ["Id", "Nombre", "Apellido","Telefono","Email","Ciudad"]
    

    return render_template("Clientes.html", title = title, clientes = clientes, datos = datos)

@app.route('/cliente/<int:id_clientes>')
def getProduct(id_clientes):
    clientefound = [
        cliente for cliente in clientes if cliente ['id'] == id_clientes]
    if (len(clientefound) > 0 ):
        return render_template("id_cliente.html", {'cliente': clientefound[0]})
    return ({'message': 'Product Not found'})


if __name__ == "__main__":
    app.run(debug=True)