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
    return render_template('listaDeEquipos.html')

if __name__ == '__main__':
    app.run(debug=True)
