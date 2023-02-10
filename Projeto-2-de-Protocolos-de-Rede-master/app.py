from flask import Flask, render_template, request

app = Flask(__name__)

class Prod:
    def __init__(self, nomeProd, descricao, qtd, tipo):
        self.nome = nomeProd
        self.descricao = descricao
        self.qtd = qtd
        self.tipo = tipo

descricao = "Um café expresso, frequentemente referido simplesmente como expresso, é um método de preparar café através da passagem de água quente, não fervente, sob alta pressão pelo café moído."
cafe = Prod("Café Expresso", descricao, 25, "bebida")
descricao = "É especialmente preparada com recheio generoso de linguiça calabresa de primeira qualidade, queijo muçarela e orégano."
pizza = Prod("Pizza de Calabresa", descricao, 5, "comida")
produtos = [cafe, pizza]

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html", produtos=produtos)

@app.route("/cadastrar", methods = ["GET", "POST"])
def form():
    add = False
    nomeProduto = ''
    if (request.method == "POST"):
        nomeProd = request.form.get("nomeProd")
        descricao = request.form.get("descricaoProd")
        qtd = request.form.get("qtdProd")
        tipo = request.form.get("tipo")
        p = Prod(nomeProduto, descricao, qtd, tipo)
        produtos.append(p)
        add = True
    return render_template("cadastrar.html", resAdd=add, nomeProd=nomeProd)

if __name__ == "__main__":
    app.run(debug=True)