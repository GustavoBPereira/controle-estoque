let lista_itens = [];

function adicionarItem(nome, quantidade) {
    if(nome == '' || quantidade == ''){
        //pass
    }else{
        lista_itens.push([nome, quantidade])
        document.querySelector('input#lista_de_itens').value = lista_itens;

        let quantidade_itens = parseInt(document.querySelector('input#quantidade_itens').value) + 1;

        document.querySelector('input#quantidade_itens').value = quantidade_itens.toString();
        document.querySelector('tbody#lista-itens').innerHTML += '<tr id=' +'item-'+quantidade_itens.toString()+ '><th scope="row">' + nome + '</th><th>' + quantidade + '</th></tr>';
        document.querySelector('input#produto_adicionado').value = '';
        document.querySelector('input#quantidade_adicionada').value = '';
    }
}