function gerarCartao(dadosCartao){

    const daddy = document.getElementById("abrigo-cards");
    const baby = document.createElement("div");
    const img = document.createElement("img");  
    const corpinho = document.createElement("div");
    const title = document.createElement("h5");
    const preco = document.createElement("p");
    const botaozinho = document.createElement("button");
    const elementos = [baby,img,corpinho,title,preco,botaozinho];
    const classesOfMyBoyfriend = [
        "card mb-4 box-shadow",
        "card-img-top",
        "card-body",
        "card-title",
        "card-text",
        "btn btn-success"
    ];
    
    botaozinho.textContent = 'Comprar';
    title.textContent = dadosCartao.food_name;
    preco.textContent = "R$"+dadosCartao.price;
    img.src = dadosCartao.caminho_img;
    baby.style = "width: 18rem;background-color: rgb(255, 221, 227);"

    corpinho.append(title,preco,botaozinho);
    baby.append(img,corpinho);
    daddy.append(baby);

    classesOfMyBoyfriend.forEach(arrozAGrelo => {
        const indexDaClasse = classesOfMyBoyfriend.indexOf(arrozAGrelo);
        elementos[indexDaClasse].className = arrozAGrelo;
    });
}

fetch("http://localhost:3000/cardapio").
then(dadosCis => dadosCis.json()).
then(dadosTrans => {
    dadosTrans.forEach(produto => {
        gerarCartao(produto)
    });
});