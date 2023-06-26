from flask import Flask, render_template
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

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/contraseña')
def contraseña():
    return render_template('contraseña.html')



if __name__ == '__main__':
    app.run(debug=True)
