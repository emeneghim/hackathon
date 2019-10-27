from flask import Flask , render_template, request, redirect, session
from models import Usuario, Veiculo, Camera

app = Flask(__name__)
app.config['SECRET_KEY']="kjNBKJBWF87t23hbjh%$#@(*%$*zxfgafdgadfgadfgadfga434wedf344g"

@app.route("/")
def recepcao():
    return render_template ("inicio.html", title = "TrackSoft")

@app.route("/perfil")
def perfil():
    lista = Usuario.select()
    return render_template ("perfil.html", title = "Perfil", lista = lista, id_usuario = session['usuario'])

@app.route("/form_cadastro_veiculo")
def form_cadastro_veiculo():
    return render_template ("form_cadastro_veiculo.html", title = "Cadastro de Veículo")

@app.route("/form_cadastro_camera")
def form_cadastro_camera():
    return render_template ("form_cadastro_camera.html", title = "Cadastro de Câmera")

@app.route("/form_cadastro_usuario")
def form_cadastro_usuario():
    return render_template ("form_cadastro_usuario.html", title = "Cadastro de Usuário")

@app.route("/form_login")
def form_login():
    return render_template ("form_login.html", title = "Login")

@app.route("/cadastro_usuario",  methods = ["POST"])
def cadastro_usuario():
    nome = request.form["nome"]
    cpf = request.form["CPF"]
    telefone = request.form["telefone"]
    senha1 = request.form["senha1"]
    senha2 = request.form["senha2"]
    foto_usuario = request.form["foto"]
    if senha1 == senha2:
        novo_usuario = Usuario(nome = nome, cpf = cpf, senha = senha1, foto = "/static/" + foto_usuario, telefone = telefone)
        novo_usuario.save()
        session['usuario'] = nome
        return redirect("/")

@app.route('/login', methods = ["POST"])
def login():
    cpf = request.form["CPF"]
    senha = request.form["senha"]
    busca = Usuario.get_or_none(cpf=cpf, senha = senha)
    lista = Usuario.select()
    for a in lista:
        if a.cpf == cpf:
            pessoa = a.nome
    if busca != None:
        session['usuario'] = pessoa
        render_template('inicio.html')
    
    return redirect("/")

@app.route("/cadastro_veiculo",  methods = ["POST"])
def cadastro_veiculo():
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    cor = request.form["cor"]
    placa = request.form["placa"]
    ano = request.form["ano"]
    foto = request.form["foto"]
    descricao = request.form["descricao"]

    novo_veiculo = Veiculo(marca = marca,modelo = modelo,cor = cor, placa = placa, ano = ano, foto = "/static/" + foto, descricao = descricao)
    novo_veiculo.save()
    return redirect("/perfil")

        
@app.route("/cadastro_camera",  methods = ["POST"])
def cadastro_camera():
    identificador = request.form["identificador"]
    rua = request.form["rua"]
    numero = request.form["numero"]
    bairro = request.form["bairro"]
    complemento = request.form["complemento"]
    cidade = request.form["cidade"]
    UF = request.form["UF"]

    nova_camera = Camera(identificador = identificador, rua = rua, numero = numero,bairro = bairro, complemento = complemento, cidade = cidade, UF = UF)
    nova_camera.save()
    return redirect("/perfil")

@app.route("/logout")
def logout():
    session.pop('usuario')
    return redirect ("/")

app.run(debug=True, host="0.0.0.0")