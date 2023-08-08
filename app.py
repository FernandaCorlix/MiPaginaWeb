from flask import Flask, render_template,request,redirect
import mysql.connector
import config as c


app = Flask('app',template_folder='app/vistas',static_folder='app/static')
config = {
    'host': c.host,
    'database': c.database,
    'user': c.user,
    'password': c.contrasenia
}
connectionPool = mysql.connector.pooling.MySQLConnectionPool(pool_name="my_pool", pool_size=10, **config)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('registro.html')
    elif request.method == 'POST':
        usuario = request.form['nombre']
        contrasenia = request.form['contrasenia']
        sexo = request.form['sexo']
        conexion = connectionPool.get_connection()
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO jugadores (NombreUsuario, contrasenia, sexo, esAdmin) VALUES (%s, %s, %s, %s)"
            val = (usuario, contrasenia, sexo, False)
            cursor.execute(sql, val)
            conexion.commit()
        finally:
            if conexion:
                conexion.close()
        return redirect('/inicio')

@app.route('/contraseña')
def contraseña():
    return render_template('contraseña.html')

@app.route('/jugadores')
def jugadores():
    conexion = connectionPool.get_connection()
    try:
        cursor = conexion.cursor()
        sql = "Select * from jugadores"
        cursor.execute(sql)
        listaJugadores = cursor.fetchall()
    finally:
        if conexion:
            conexion.close()
    return render_template('jugadores.html',listaJugadores = listaJugadores)

@app.route('/listaDeEquipos')
def listaDeEquipos():
    conexion = connectionPool.get_connection()
    try:
        cursor = conexion.cursor()
        sql = "Select * from Equipo"
        cursor.execute(sql)
        listaEquipos = cursor.fetchall()
    finally:
        if conexion:
            conexion.close()
    return render_template('listaDeEquipos.html', listaEquipos = listaEquipos)

@app.route('/listaDeEquipos/borrar/<int:equipo_id>', methods=['POST'])
def borrarEquipo(equipo_id):
    conexion =connectionPool.get_connection()
    try:
        cursor = conexion.cursor()
        sql = "Delete from Equipo where EquipoID = (%s)"
        cursor.execute(sql,(equipo_id,))
        conexion.commit()
    finally:
        if conexion:
            conexion.close()
    return redirect('/listaDeEquipos')

@app.route('/crearEquipo', methods=['GET', 'POST'])
def crearEquipo():
    if request.method == 'GET':
        return render_template('crearEquipo.html')
    elif request.method == 'POST':
        conexion = connectionPool.get_connection()
        if conexion is None:
            return "Unable to acquire a database connection"
    
        cursor = conexion.cursor()
        nombreEquipo = request.form['nombre']
        sql = "Select * from Equipo where nombreEquipo = %s"
        cursor.execute(sql,(nombreEquipo,))
        Equipos = cursor.fetchall()
        if len(Equipos) > 0:
            if conexion:
                conexion.close()
            #Equipo ya existe
            return "El equipo ya existe"
        else:
            print("Llegue aqui")
            sql = "Insert into Equipo (nombreEquipo) VALUES (%s)"
            cursor.execute(sql,(nombreEquipo,))
            conexion.commit()
            if conexion:
                conexion.close()
            return redirect("/listaDeEquipos")  

if __name__ == '__main__':
    app.run(debug=True)
