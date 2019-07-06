from flask import render_template, url_for, request, redirect, flash
from sqlalchemy.exc import IntegrityError

from config import app
from db import db, Estoque

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/produtos')
def produtos():
    produtos = Estoque.query.order_by(Estoque.nome).all()
    return render_template('produtos.html', produtos=produtos)


@app.route('/produtos_faltando')
def produtos_faltando():
    produtos = Estoque.query.order_by(Estoque.nome).all()
    produtos_em_falta = []

    for produto in produtos:
        if int(produto.quantidade_estoque) < int(produto.quantidade_minima):
            produtos_em_falta.append(produto)

    return render_template('produtos_faltando.html', produtos=produtos_em_falta)


@app.route('/novo_produto/<erro_nome>', methods=['GET'])
def novo_produto(erro_nome):
    if erro_nome == 'sim':
        #TODO ALERT
        print('sim')
    return render_template('novo_produto.html')


@app.route('/criar_produto', methods=['POST'])
def criar_produto():

    nome = request.form['nome']
    valor_compra = request.form['valor_compra']
    valor_venda = request.form['valor_venda']
    quantidade_estoque = request.form['quantidade_estoque']
    quantidade_minima = request.form['quantidade_minima']

    novo_produto = Estoque(
        nome=nome, valor_compra=valor_compra, valor_venda=valor_venda, 
        quantidade_estoque=quantidade_estoque, quantidade_minima=quantidade_minima)
    try:
        db.session.add(novo_produto)
        db.session.commit()
    except IntegrityError:
        return redirect(url_for('novo_produto', erro_nome='sim'))
    return redirect(url_for('produtos'))


@app.route('/alterar_produto/<id>')
def alterar_produto(id):
    produto_para_modificar = Estoque.query.filter_by(id=id).first()
    return render_template('alterar_produto.html', produto=produto_para_modificar)


@app.route('/modificar', methods=['POST'])
def modificar():
    id = request.form['id']
    produto_para_modificar = Estoque.query.filter_by(id=id).first()
    produto_para_modificar.nome = request.form['nome']
    produto_para_modificar.valor_compra = request.form['valor_compra']
    produto_para_modificar.valor_venda = request.form['valor_venda']
    produto_para_modificar.quantidade_estoque = request.form['quantidade_estoque']
    produto_para_modificar.quantidade_minima = request.form['quantidade_minima']

    db.session.add(produto_para_modificar)
    db.session.commit()

    return redirect(url_for('produtos'))



@app.route('/excluir_produto/<id>')
def excluir_produto(id):
    produto_para_remover = Estoque.query.filter_by(id=id).first()
    db.session.delete(produto_para_remover)
    db.session.commit()
    return redirect(url_for('produtos'))

@app.route('/venda')
def venda():
    produtos = Estoque.query.all()
    return render_template('venda.html', produtos=produtos)

@app.route('/finalizar_venda', methods=['POST'])
def finalizar_venda():
    lista_venda = request.form['lista_de_itens'].split(',')
    #[produto] = nome do produto, [produto+1] = quantidade vendida do produto...
    for produto in range(0,len(lista_venda), 2):
        produto_para_vender = Estoque.query.filter_by(nome=lista_venda[produto]).first()
        if produto_para_vender is not None: 
            if int(produto_para_vender.quantidade_estoque) >= int(lista_venda[produto+1]):
                produto_para_vender.quantidade_estoque =  str(int(produto_para_vender.quantidade_estoque)-int(lista_venda[produto+1]))
                db.session.add(produto_para_vender)
                db.session.commit()
        
    return redirect(url_for('produtos'))

@app.route('/reestoque')
def reestoque():
    produtos = Estoque.query.all()
    return render_template('reestoque.html', produtos=produtos)

@app.route('/compra', methods=['post'])
def compra():
    lista_venda = request.form['lista_de_itens'].split(',')
    #[produto] = nome do produto, [produto+1] = quantidade adicionada do produto...
    for produto in range(0,len(lista_venda), 2):
        produto_para_adicionar = Estoque.query.filter_by(nome=lista_venda[produto]).first()
        if produto_para_adicionar is not None: 
            produto_para_adicionar.quantidade_estoque = str(int(lista_venda[produto+1]) + int(produto_para_adicionar.quantidade_estoque))
            db.session.add(produto_para_adicionar)
            db.session.commit()
    return redirect(url_for('produtos'))