from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/ship_wars')
def ship_wars():
    return render_template('project_ship_wars.html')


app.run(debug=True)
