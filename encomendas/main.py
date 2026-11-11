from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.get("/encomendas")
def consultar_encomendas():
    resposta = requests.get("http://produtos:5000/produtos")
    produtos = resposta.json()
    return produtos

if __name__ == "__main__":
    app.run(host="0.0.0.0")
