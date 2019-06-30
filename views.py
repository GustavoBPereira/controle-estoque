from flask import render_template, url_for, request, redirect
from sqlalchemy.exc import IntegrityError

from config import app
from db import db, Estoque

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/produtos')
def produtos():
    produtos = Estoque.query.all()
    return render_template('produtos.html', produtos=produtos)


@app.route('/produtos_faltando')
def produtos_faltando():
    produtos = Estoque.query.all()
    produtos_em_falta = []

    for produto in produtos:
        if int(produto.quantidade_estoque) < int(produto.quantidade_ideal):
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
    quantidade_ideal = request.form['quantidade_ideal']

    novo_produto = Estoque(
        nome=nome, valor_compra=valor_compra, valor_venda=valor_venda, 
        quantidade_estoque=quantidade_estoque, quantidade_ideal=quantidade_ideal)
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
    produto_para_modificar.quantidade_ideal = request.form['quantidade_ideal']

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
    produto = request.form['produto_vendido']
    quantidade = request.form['quantidade_vendida']
    print('produto = ', produto, '\n', 'quantidade =', quantidade, '\n')
    return redirect(url_for('produtos'))