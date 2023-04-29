#Importacion de modulos
from flask import Flask, render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json, datetime
from sqlalchemy.orm import relationship

#Configuracion y conexion a la DB
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/tecnoglass'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)


#Modelos de las DB
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    direccion=db.Column(db.String(100))
    telefono=db.Column(db.Integer)
    nacionalidad=db.Column(db.String(100))
    correo=db.Column(db.String(100))
    user=db.relationship('Order', backref='user')
    

    def __init__(self,id,nombre,direccion,telefono,nacionalidad,correo):
        self.id = id
        self.nombre = nombre
        self.direccion= direccion
        self.telefono=telefono
        self.nacionalidad=nacionalidad
        self.correo=correo

class Order(db.Model):
    id_order=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.DateTime, default=datetime.datetime.now())
    largo=db.Column(db.Integer)
    ancho=db.Column(db.Integer)
    estado=db.Column(db.String(100))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,id_order,fecha,largo,ancho,estado,user_id):
        self.id_order = id_order
        self.fecha= fecha
        self.largo= largo
        self.ancho=ancho
        self.estado=estado
        self.user_id= user_id


#Esquemas
class UserSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','direccion','telefono','nacionalidad','correo','user_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class OrderSchema(ma.Schema):
    class Meta:
        fields=('id_order','fecha','largo','ancho','estado','user_id')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

#-----------------------
#Rutas de las APIs
#------------------------

#Agregar Usuario
@app.route('/addUser', methods=['POST'])
def add_user():
    id=int(request.form['id'])
    nombre=request.form['nombre']
    direccion=request.form['direccion']
    telefono=request.form['telefono']
    nacionalidad=request.form['nacionalidad']
    correo=request.form['correo']

    #Validacion de Formulario llenos
    if(id=='' or nombre=='' or direccion=='' or telefono=='' or nacionalidad=='' or correo==''):
        return 'PorFavor llene todos los campos'
    else:  
      IdUser= User.query.get(id)
      if IdUser is None:
            new_User = User(id,nombre,direccion,telefono,nacionalidad,correo)
            db.session.add(new_User)
            db.session.commit()
            return user_schema.jsonify(new_User)
      else:
        return 'Usuario ya registrado'

#Listar los Usuarios
@app.route('/listUser',methods=['GET'])
def list_user():
    users= User.query.all()
    result=users_schema.jsonify(users)

    return result
    
#Actualizar Usuarios
@app.route('/editUser/<id>',methods=['PUT'])
def edit_user(id):
    user= User.query.get(id)
    if user is None:
        return 'Usuario no encontrado, verificar Id'
    else:   
        nombre=request.form['nombre']
        direccion=request.form['direccion']
        telefono=request.form['telefono']
        nacionalidad=request.form['nacionalidad']
        correo=request.form['correo']

        user.nombre=nombre
        user.direccion=direccion
        user.telefono=telefono
        user.nacionalidad=nacionalidad
        user.correo=correo
        db.session.commit()
        return "Usuario Actualizado"

#Eliminar Usuario
@app.route('/deleteUser/<id>',methods=['DELETE'])
def delete_user(id):
    Iduser= User.query.get(id)
    if Iduser is None:
        return 'Usuario no encontrado, verificar Id'
    else:   
        db.session.delete(Iduser)
        db.session.commit()
        return "Usuario eliminado"
    
#------------------------------------------------------
#Agregar Orden
@app.route('/addOrder', methods=['POST'])
def add_Order():
    id_order=int(request.form['id'])
    largo=int(request.form['largo'])
    ancho=int(request.form['ancho'])
    user_id=int(request.form['user_id'])
    

    #Validacion de Formulario llenos
    if(id_order=='' or largo=='' or ancho=='' or user_id==''):
        return 'PorFavor llene todos los campos'
    else:  
        new_Order = Order(id_order,datetime.datetime.now(),largo,ancho,"espera",user_id)
        db.session.add(new_Order)
        db.session.commit()
        return "Orden agregada exitosamente"
    
@app.route('/listOrder',methods=['GET'])
def list_order():
    order= Order.query.all()
    result=orders_schema.jsonify(order)

    return result
    
#Aprobar Orden
@app.route('/AprobOrder/<id>',methods=['PUT'])
def aprob_order(id):
    order= Order.query.get(id)
    if order is None:
        return 'Orden no encontrada, verificar No Orden'
    else:   
        estado=request.form['estado']
        order.estado=estado
        db.session.commit()
        return "Orden Aprobada"
    
#Cancelar Orden
@app.route('/CancelOrder/<id>',methods=['PUT'])
def cancel_order(id):
    order= Order.query.get(id)
    if order is None:
        return 'Orden no encontrada, verificar No Orden'
    else:   
        estado=request.form['estado']
        order.estado=estado
        db.session.commit()
        return "Orden Cancelada"




