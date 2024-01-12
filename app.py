import json
from flask import Flask, request, redirect, flash, jsonify,send_from_directory
import controlador.controlador_contacto as controlador_contacto
import clase.clase_contacto as clase_contacto
from flask_cors import CORS  # Importa la extensión
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
CORS(app)
app.debug = True
UPLOAD_FOLDER = 'imagen'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/api_obtenercontactos")
def api_obtenercontactos():
    try:
        contactos = controlador_contacto.obtener_contactos()
        listaserializable = []
        for contacto in contactos:
            miobj = clase_contacto.Contacto(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4], contacto[5], contacto[6],contacto[7])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})
    
@app.route("/api_obtenercontacto/<int:id>")
def api_obtenercontacto(id):
    try:
        contacto = controlador_contacto.obtener_contactoid(id)
        listaserializable = []
        miobj = clase_contacto.Contacto(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4], contacto[5], contacto[6],contacto[7])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_eliminarcontacto", methods=["POST"])
def api_eliminarcontacto():
    try:
        id_contacto = request.json["id"]
        controlador_contacto.eliminar_contacto(id_contacto)
        return jsonify({"Mensaje": "Contacto eliminado correctamente"})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"Mensaje": "Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})
    
@app.route("/api_actualizarcontacto", methods=["POST"])
def api_actualizarcontacto():
    try:
        id = request.form["id"]
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        web = request.form["web"]
        profesion = request.form["profesion"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        print(nombres)

        if 'foto' not in request.files:
            return jsonify({"Mensaje": "No se proporcionó ninguna imagen"}), 400

        file = request.files['foto']

        if file.filename == '':
            return jsonify({"Mensaje": "Nombre de archivo vacío"}), 400

        print(file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            foto_url = f'http://127.0.0.1:8000/{filename}'  # Ajusta la URL según sea necesario
        else:
            return jsonify({"Mensaje": "Formato de archivo no permitido"}), 400

        # Resto del código para manejar la información del contacto
        controlador_contacto.actualizar_contacto(id,nombres, apellidos, web, profesion, telefono, email, foto_url)

        return jsonify({"Mensaje": "Contacto registrado correctamente"})
    except Exception as e:
        print(str(e))
        return jsonify({"Mensaje": "Error interno. Llame al Administrador de sistemas (+51) 969 696 969"}), 500

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/api_guardarcontacto", methods=["POST"])
def api_guardarcontacto():
    try:
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        web = request.form["web"]
        profesion = request.form["profesion"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        print(nombres)

        if 'foto' not in request.files:
            raise ValueError("No se proporcionó ninguna imagen")

        file = request.files['foto']

        if file.filename == '':
            raise ValueError("Nombre de archivo vacío")

        print(file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            foto_url = f'http://127.0.0.1:8000/{filename}'  # Ajusta la URL según sea necesario
        else:
            raise ValueError("Formato de archivo no permitido")

        # Resto del código para manejar la información del contacto
        controlador_contacto.insertar_contacto(nombres, apellidos, web, profesion, telefono, email, foto_url)

        return jsonify({"Mensaje": "Contacto registrado correctamente"})

    except ValueError as ve:
        print(str(ve))
        return jsonify({"Mensaje": str(ve)}), 400

    except Exception as e:
        print(str(e))
        return jsonify({"Mensaje": "Error interno. Llame al Administrador de sistemas (+51) 969 696 969"}), 500
app.static_folder = 'imagen'

@app.route('/<filename>')
def send_file(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
