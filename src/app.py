from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from models import db, Practicante, Administrador, Region, Provincia, Comuna, Empresa, Oferta, Postulacion
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
Migrate(app, db)

@app.route('/')
def root():
    return "hello world"

@app.route('/api/user-register', methods=['POST'])
def register_user():
    nombre = request.json.get("nombre")
    apellido = request.json.get("apellido")
    email = request.json.get("email")
    password = request.json.get("password")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    comuna_id = request.json.get("comuna_id")

    practicante = Practicante()
    practicante.nombre = nombre
    practicante.apellido = apellido
    practicante.email = email
    practicante.password = password
    practicante.fecha_nacimiento = fecha_nacimiento
    practicante.comuna_id = comuna_id

    practicante.save()

    return jsonify(practicante.serialize())

@app.route('/api/empresa-register', methods=['POST'])
def register_empresa():
    razon_social = request.json.get("razon_social")
    email = request.json.get("email")
    password = request.json.get("password")
    telefono = request.json.get("telefono")
    
    empresa = Empresa()
    empresa.razon_social = razon_social
    empresa.email = email
    empresa.password = password
    empresa.telefono = telefono
   
    empresa.save()

    return jsonify(empresa.serialize())

@app.route('/create-oferta', methods=['POST'])
def create_oferta():
    titulo = request.json.get("titulo")
    area = request.json.get("area")
    carrera_requerida = request.json.get("carrera_requerida")
    fecha_inicio = request.json.get("fecha_inicio")
    fecha_termino = request.json.get("fecha_termino")
    comuna_id = request.json.get("comuna_id")
    empresa_id = request.json.get("empresa_id")
    
    oferta = Oferta()
    oferta.titulo = titulo
    oferta.area = area
    oferta.carrera_requerida = carrera_requerida
    oferta.fecha_inicio = fecha_inicio
    oferta.fecha_termino = fecha_termino
    oferta.comuna_id = comuna_id
    oferta.empresa_id = empresa_id
   
    oferta.save()

    return jsonify(oferta.serialize())

@app.route('/generate-postulacion', methods=['POST'])
def generate_postulacion():
    fecha_postulacion = request.json.get("fecha_postulacion")
    practicante_id = request.json.get("practicante_id")
    oferta_id = request.json.get("oferta_id")
    
    postulacion = Postulacion()
    postulacion.fecha_postulacion = fecha_postulacion
    postulacion.practicante_id = practicante_id
    postulacion.oferta_id = oferta_id
   
    postulacion.save()

    return jsonify(postulacion.serialize())

@app.route('/api/admin-register', methods=['POST'])
def register_admin():
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    email = request.json.get('email')
    password = request.json.get('password')

    administrador = Administrador()
    administrador.nombre = nombre
    administrador.apellido = apellido
    administrador.email = email
    administrador.password = password

    administrador.save()

    return jsonify(administrador.serialize())

#Devuelve todas las regiones

@app.route('/region', methods=['GET'])
def showRegion():
    allRegion = Region.query.all()
    allRegion = list(map(lambda x: x.serialize(), allRegion))

    return jsonify(allRegion)

@app.route('/provincia', methods=['GET'])
def showProvincia():
    region_id_req = request.json.get("region_id")
    allProvincia = Provincia.query.filter_by(region_id = region_id_req)
    allProvincia = list(map(lambda x: x.serialize(), allProvincia))

    return jsonify(allProvincia)

@app.route('/comuna', methods=['GET'])
def showComuna():
    comuna_id_req = request.json.get("provincia_id")
    allComuna = Comuna.query.filter_by(provincia_id = comuna_id_req)
    allComuna = list(map(lambda x: x.serialize(), allComuna))

    return jsonify(allComuna)

@app.route('/practicante', methods=['GET'])
def showPracticante():
    allPracticante = Practicante.query.all()
    allPracticante = list(map(lambda x: x.serialize(), allPracticante))

    return jsonify(allPracticante)

@app.route('/practicante-id', methods=['GET'])
def showPracticante_id():
    practicante_id = request.json.get("practicante_id")
    practicante = Practicante.query.filter_by(id = practicante_id)
    practicante = list(map(lambda x: x.serialize(), practicante))

    return jsonify(practicante)

@app.route('/empresa', methods=['GET'])
def showEmpresa():
    allEmpresa = Empresa.query.all()
    allEmpresa = list(map(lambda x: x.serialize(), allEmpresa))

    return jsonify(allEmpresa)

@app.route('/empresa-id', methods=['GET'])
def showEmpresa_id():
    empresa_id = request.json.get("empresa_id")
    empresa = Empresa.query.filter_by(id = empresa_id)
    empresa = list(map(lambda x: x.serialize(), empresa))

    return jsonify(empresa)

@app.route('/oferta', methods=['GET'])
def showOferta():
    allOferta = Oferta.query.all()
    allOferta = list(map(lambda x: x.serialize(), allOferta))

    return jsonify(allOferta)

@app.route('/oferta-id', methods=['GET'])
def showOferta_id():
    oferta_id = request.json.get("oferta_id")
    oferta = Oferta.query.filter_by(id = oferta_id)
    oferta = list(map(lambda x: x.serialize(), oferta))

    return jsonify(oferta)

@app.route('/postulacion', methods=['GET'])
def showPostulacion():
    allPostulacion = Postulacion.query.all()
    allPostulacion = list(map(lambda x: x.serialize(), allPostulacion))

    return jsonify(allPostulacion)

@app.route('/postulacion-id', methods=['GET'])
def showPostulacion_id():
    postulacion_id = request.json.get("postulacion_id")
    postulacion = Postulacion.query.filter_by(id = postulacion_id)
    postulacion = list(map(lambda x: x.serialize(), postulacion))

    return jsonify(postulacion)

if __name__ == '__main__':
    app.run()