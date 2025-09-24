from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html')

if __name__ == "__main__":
    # Obtener el puerto asignado por Render, si no existe usa 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
