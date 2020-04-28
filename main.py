# 1.- utilizamos la libreria de flask
from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
# 2.- crear una aplicacion
app = Flask(__name__)

# Configuracion a MySQL
# 1.-Servidor a conectarse
app.config['MYSQL_HOST'] = 'localhost'
# 2.-Usuario a conectarse
app.config['MYSQL_USER'] = 'root'
# 3.-Password del usuario
app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_PORT'] = 33067  si tenemos un puerto creado ojo sin el ''
app.config['MYSQL_PORT'] = 3306
# 4.-La BD a conectarme
app.config['MYSQL_DB'] = 'bdresumen'
# 5.-Configurar la informacion a conectarse en modo diccionario
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# Creo el objeto mysql que tendra la aplicacion conectada al servidor
mysql = MySQL(app)

# 3.- crear rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cursos') #http://127.0.0.1:5000/cursos
def cursos():
    # Creando el cursor que se conectara al servidor
    cur = mysql.connection.cursor()#El metodo para crear el cursor se llama, originalmente, cursor():
    # Recuperar todos los registros de la tabla cursos
    result = cur.execute("select * from tbl_cursos;") # result es una variable cualquiera
    # Traer todos lo registros que tiene el cursor y guardarlos en el objeto cursos
    cursos = cur.fetchall()
    if result > 0: # result es una variable cualquiera
        return render_template('cursos.html', cursos=cursos)
    else:
        msg = "No Hay cursos que mostrar"
        return render_template('cursos.html', msg=msg)
    cur.close()    
    
@app.route('/alumnos')#http://127.0.0.1:5000/alumnos
def alumnos():
    cur = mysql.connection.cursor() #El metodo para crear el cursor se llama, originalmente, cursor():
    result = cur.execute("select * from tbl_alumnos;")
    alumnos = cur.fetchall()
    if result > 0:
        return render_template('alumnos.html', alumnos=alumnos)
    else:
        msg ="No hay alumnos que mostrar"
        return render_template('alumnos.html',msg=msg)
    cur.close()
    
@app.route('/profesores') #http://127.0.0.1:5000/profesores
def profesores():
    cur = mysql.connection.cursor()
    result =cur.execute("select * from tbl_profesores;")
    profesores = cur.fetchall()
    if result > 0:
        return render_template('profesores.html',profesores=profesores)
    else:
        msg="No hay profesores que mostrar!"
        return render_template('profesores.html',msg=msg)
    cur.close()

# 4.- ejecutar el servidor de ppruebas
app.run(debug=True, port=5000)
