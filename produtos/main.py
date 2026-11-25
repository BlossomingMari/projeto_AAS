from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Ténis Urban", "preco": 59.99, "tamanhos": [38, 39, 40, 41, 42]},
    {"id": 2, "nome": "Bota Classic", "preco": 79.99, "tamanhos": [37, 38, 39, 40, 41]},
]

@app.get("/")
def index():
    return render_template("index.html", produtos=produtos)

@app.get("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.get("/produtos/<int:id>")
def ver_produto(id):
    for p in produtos:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"error": "Produto não encontrado"}), 404

@app.post("/produtos")
def adicionar_produto():
    dados = request.get_json()
    novo = {
        "id": max([p["id"] for p in produtos], default=0) + 1,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "tamanhos": dados.get("tamanhos", []),
    }
    produtos.append(novo)
    return jsonify(novo), 201

@app.get("/")
def pagina_inicial():
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    