from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "marca": "Nike", "modelo": "Speedcat Croco Leather Sneakers Women", "preco": 84.00,
     "tamanhos": {"35,5": 5, "36": 4, "37": 6, "38": 3, "39": 0, "40": 3, "41": 7, "42": 2, "43": 1, "43.5": 6}},
    {"id": 2, "marca": "Adidas", "modelo": "Speedcat Wedge Sneakers Women", "preco": 130.00,
     "tamanhos": {"35,5": 5, "36": 4, "37": 6, "38": 3, "39": 0, "40": 3, "41": 7, "42": 2, "43": 1, "43.5": 6}},
    {"id": 3, "marca": "Puma", "modelo": "Speedcat OG Sneakers Unisex", "preco": 88.00,
     "tamanhos": {"35,5": 5, "36": 4, "37": 6, "38": 3, "39": 0, "40": 3, "41": 7, "42": 2, "43": 1, "43.5": 6}},
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")