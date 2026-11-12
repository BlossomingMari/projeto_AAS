from flask import Flask, render_template

app = Flask(__name__)
produtos = [
    "Sapatilhas",
    "Botas",
    "Tênis",
    "chinelos"
]

@app.get("/produtos")
def listar_produtos():
    return {"produtos": produtos}

@app.get("/")
def pagina_inicial():
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    