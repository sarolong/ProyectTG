# Aplicacion para tecnoglass

Proyecto construido bajo el framework de Python Flask , utilizando SQlalchemy ORM ,Marshmallow y mysql como motor de base de datos corriendo en el localhost


_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


Python >3.11. with `venv`
---------------------------------------
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate.bat
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy mysqlclient

## Pruebas

en el archivo app.py se encuentran las routes 

_Para add Usuario : https://localhost:5000/addUser  (recibe datos mediante un form-data METODO POST) con atributos:_
id , nombre, direccion , telefono, nacionalidad , correo

_Para listar los Usuarios : https://localhost:5000/listUser  (METODO GET)_

_Para editar Usuario : https://localhost:5000/editUser/<id>  --> se valida si existe el id requerido (METODO PUT)_

_Para ELIMINAR Usuario : https://localhost:5000//deleteUser/<id>  --> se valida si existe el id requerido (METODO DELETE)_

-------------------------------------------------------------------------------------------------------------------------
_Para add Orden : https://localhost:5000/addOrder  (recibe datos mediante un form-data METODO POST) con atributos:_
id , largo, ancho , user_id

_Para listar las ordenes : https://localhost:5000/listOrder  (METODO GET)_

_Para Aprobar Orden : https://localhost:5000/AprobOrder/<id>  --> se valida si existe el id requerido (METODO PUT)_
_Para Cancelar Orden : https://localhost:5000/CancelOrder/<id>  --> se valida si existe el id requerido (METODO PUT)_





## Autor

* **Sergio Andres Rolong Sandoval** - *Trabajo Inicial* - [afgarcia](https://github.com/afgarcia)