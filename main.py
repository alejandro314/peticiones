from flask import Flask ,request,render_template, make_response  

app=Flask(__name__)



@app.route('/buscar')
def buscar():
    producto = request.args.get('producto')
    talla = request.args.get('tamano')
    color = request.args.get('color')
    if producto is None and talla is None and color is None:
       return"faltan datospara la busqueda"
    return f"buscando {producto} de talla {talla} y color {color}"

listado=[]

@app.route("/registro", methods=["GET"])
def ruta_formulario():
    return render_template("formulario.html")

# este es el tipo de solicitud 2 que estamos enviando informacion por el body

@app.route("/registro", methods=["POST"])
def ruta_registro():
    nombre=request.form.get("estudiante")
    email=request.form.get("correo")
    passwd=request.form.get("contrasena")
    if nombre and email and passwd
    listado.append({"nombre":nombre,"correo":email,"contraseña":passwd})


    return render_template("/formulario.html",listado=listado)



return f"faltan datos"

#if __name__=="__main__":
    #app.run(debug=True)

#tipo de solicitud 3: parametros de la ruta



@app.route("/ropa/<string:producto><string:talla>")
def ruta_consulta(producto, talla):
    return f"el producto consultado es{producto}{talla}"


#tipo de solicitud 4: headers http


@app.route("/ver-headers")
def ruta_headers():
    navegador=request.headers.get("user-agent")
    return f"el navegador que hace la peticion es {navegador}"

#tipo de solicitud 5. manejo de cookies

@app.route("/crear-cookie")
def crear_cookie():
    respuesta=make_response("cookie creada")
    respuesta.set_cookie("usuario_logeado","True")
    return respuesta

@app.route("/leer_cookie")
def leer_cookie():
    valor=request.cookies.get ("usuario_logeado")
    return f"el valor de la cookie es: {valor}"