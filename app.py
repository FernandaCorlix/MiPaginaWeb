from flask import Flask, render_template

app = Flask('app',template_folder='app/vistas',static_folder='app/static')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
