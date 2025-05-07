from flask import Flask, render_template,request

app=Flask(__name__)



@app.route('/buscar')
def buscar():
    producto = request.args.get('producto')
    talla = request.args.get('tamano')
    color = request.args.get('color')
    if producto is None and talla is None and color is None:
       return"faltan datospara la busqueda"
    return f"buscando {producto} de talla {talla} y color {color}"



@app.route("/registro", methods=["GET"])
def ruta_formulario():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"])
def ruta_registro():
    nombre=request.form.get("estudiante")
    email=request.form.get("correo")
    passwd=request.form.get("contrasena")
    return f"usuario registrado:{nombre},{email},{passwd}"

if __name__=="__main__":
    app.run(debug=True)

































