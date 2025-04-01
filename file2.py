from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    t = "Заготовка"
    return render_template('base.html', title=t)

if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')