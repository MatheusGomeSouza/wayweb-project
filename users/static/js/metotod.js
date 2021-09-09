var url = "http://127.0.0.1:8000/prod/prod/";//Sua URL

var xhttp = new XMLHttpRequest();
xhttp.open("GET", url, false);

xhttp.onreadystatechange = function(){//Função a ser chamada quando a requisição retornar do servidor
    if ( xhttp.readyState == 4 && xhttp.status == 200 ) {//Verifica se o retorno do servidor deu certo
        console.log(xhttp.responseText);
    }
}

xhttp.send();//A execução do script pára aqui até a requisição retornar do servidor
