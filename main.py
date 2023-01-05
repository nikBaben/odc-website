from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('menu.html')
print("frontend branch1")


for i in range(1000):
    pass

app.run(debug=True)


