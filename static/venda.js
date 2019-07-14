let lista_itens = [];

function adicionarItem(nome, quantidade) {
    if(nome == '' || quantidade == ''){
        //pass
    }else{
        lista_itens.push([nome, quantidade])
        document.querySelector('input#lista_de_itens').value = lista_itens;

        colocarNaTabela(nome, quantidade);
        limparFormulario();
        
    }
}


function limparFormulario() {
    document.querySelector('input#produto_vendido').value = '';
    document.querySelector('input#quantidade_vendida').value = '';
}

function colocarNaTabela(nome, quantidade){
    let ultimo_item = parseInt(document.querySelector('input#ultimo_item').value) + 1;

    document.querySelector('input#ultimo_item').value = ultimo_item.toString();
    document.querySelector('tbody#lista-itens').innerHTML += '<tr id=item-'+ultimo_item.toString()+
                                                                '><th scope="row">' + nome + '</th>'+
                                                                '<th>' + quantidade + '</th>'+
                                                                '<th><button id='+ultimo_item.toString()+' onclick="removerItem(this.id)"><img src="static/remover.png"></button></th>'+
                                                             '</tr>';
                    
}

function removerItem(id_produto){
    // remover do front
    document.querySelector('tr#item-'+id_produto).remove();

    // remover da lista
    lista_itens.splice(parseInt(id_produto)-1, 1, []);
    document.querySelector('input#lista_de_itens').value = lista_itens;
}