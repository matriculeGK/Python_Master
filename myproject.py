from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenue sur l'application Flask personnalisée !"

@app.route('/nouvelle-page')
def nouvelle_page():
    return "Voici une nouvelle page personnalisée !"

if __name__ == '__main__':
    app.run()from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
