from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

cnpj = CNPJ()
cpf = CPF()
#app = Flask('Minha app')
app = Flask(__name__)

# rota + função 

# / - home page
@app.route('/')
def home():
    return render_template("home.html")

#/contato - página de contato

@app.route('/contato')
def contato():
    return render_template("contato.html")

#/produtos - pagina de produtos

@app.route('/produtos')
def produtos():
    lista_produtos = [
        {'nome': 'chic', 'descricao': 'anita'},
        {'nome': 'astral', 'descricao': 'risque'},
        {'nome': 'dengo', 'descricao': 'impala'}
    ]
    return render_template("produtos.html", produtos = lista_produtos)

@app.route('/servicos')
def servicos():
    return "<h1> Nossos serviços </h1>"

@app.route("/gerar-cpf")
def gerar_cpf():
    return f"CPF: {cpf.generate(True)}"

@app.route("/gerar-cnpj")
def gerar_cnpj():
    return f"CNPJ: {cnpj.generate(True)}"


