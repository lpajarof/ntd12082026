from flask import Flask, render_template

app = Flask(__name__)

name = "Elba Zurita"
contacto = "elba.zurita@example.com"

@app.route("/")
def hello_world():
    return render_template('index.html', person=name, contacto=contacto)

if __name__ == "__main__":
    app.run(debug=True)