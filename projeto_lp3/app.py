from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
        {'nome': 'chic', 'descricao': 'anita', 'url' : 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.maisvaidosa.com.br%2Fesmalte-anita-chic-glitter-10734-p1010921&psig=AOvVaw1Fm2BKRRYx2GJqdxhHPyK7&ust=1718993402172000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCJD-rMrj6oYDFQAAAAAdAAAAABAE'},
        {'nome': 'astral', 'descricao': 'risque', 'url': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.risque.com.br%2Fprodutos%2Fesmalte-risque-regular-astral%2F&psig=AOvVaw0BDkqpAfXzf4mtQtV1JgVk&ust=1718993250744000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCPiQsYLj6oYDFQAAAAAdAAAAABAE'},
        {'nome': 'dengo', 'descricao': 'impala', 'url': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Famendoacores.com.br%2Fprodutos%2Fesmalte-dengo-perolado-impala%2F&psig=AOvVaw2621CHbvOFMSpRmqthekWj&ust=1718993383135000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCPDWoMHj6oYDFQAAAAAdAAAAABAI'}
    ]


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
    
    return render_template("produtos.html", produtos = lista_produtos)

@app.route('/servicos')
def servicos():
    return "<h1> Nossos serviços </h1>"


@app.route("/gerarcpf")
def gerar_cpf():
    cpf = CPF()
    cpf_retorno = cpf.generate(True)
    return render_template("cpf.html", cpf = cpf_retorno )



@app.route("/gerarcnpj")
def gerar_cnpj():
    cnpj = CNPJ()
    cnpj_retorno = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = cnpj_retorno )


@app.route('/termosdeuso')
def termosdeuso():
    return render_template("termosdeuso.html")

@app.route('/politicadeprivacidade')
def politicadeprivacidade():
    return render_template("politicadeprivacidade.html")

@app.route('/privacidade')
def privacidade():
    return render_template("privacidade.html")

#GET /produtos/cadastro devolver o formulario

@app.route('/produtos/cadastro')
def cadastro_produto():
    return render_template('cadastro_produto.html')

#POST /produtos que vai lidar com os dados enviados pelo formulario
#acessar o objeto request

@app.route('/produtos', methods = ['POST'])
def salvar_produto():
    #pegando os valores digitados no  formulario que estao na request
    nome = request.form['nome']
    descricao = request.form['descricao']
    
    #cria um novo prroduto, ou seja, um novo dict
    produto = {'nome': nome, 'descricao': descricao, 'url': ''}
    
    #adiciona um novo produto na lista
    lista_produtos.append(produto)
    
    #devolvo o template com o novo produto
    return render_template('produtos.html', produtos = lista_produtos)


app.run()


