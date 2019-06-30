function criar_form() {
    const quantidade_de_produtos = document.getElementById("quantidade_de_produtos").value
    var form_princial = document.querySelector('div#form_princial')
    form_princial.innerHTML +=
}


// <form name="form" action="{{ url_for('finalizar_venda') }}" method="POST" enctype="multipart/form-data">

// <label for="produto_vendido">PRODUTO</label>
// <input list="produtos" name="produto_vendido" id="produto_vendido">
// <datalist id="produtos">
//     {% for produto in produtos %}
//         <option value="{{ produto.nome }}">
//     {% endfor %}
// </datalist>

// <label for="quantidade">QUANTIDADE VENDIDA</label>
// <input type="number" name="quantidade_vendida" id="quantidade_vendida">

// <br>    
// <input type="submit">

// </form>