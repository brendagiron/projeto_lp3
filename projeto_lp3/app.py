from flask import Flask

#app = Flask('Minha app')
app = Flask(__name__)

# rota + função 

# / - home page
@app.route('/')

def home ():
    return '<h1> Home Page </h1>'

#/contato - página de contato

@app.route('/contato')
def contato():
    return '<h1>Contato</h1>'

#/produtos - pagina de produtos

@app.route('/produtos')
def produtos():
    return '<h1>Produtos</h1>'