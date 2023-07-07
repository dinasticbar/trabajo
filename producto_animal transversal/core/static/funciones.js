function validarlleno(input) {
    var dato = document.querySelector(input);
    if (dato.value.length > 5 && dato.value.length <25) {
        dato.classList.remove("error");
    } else {
        dato.classList.add("error")
    }
}

function validarcontrasena(){
    var con= document.querySelector('#contrasena,#contrasema');
    if(con.value.length >= 5 && con.value.length <= 17 ){
        con.classList.remove("error");
    }else{
        con.classList.add("error");
    }
}

function validarnombre(input){
    var nom= document.querySelector(input)
    if(nom.value.length > 2 && nom.value.length <14){
    nom.classList.remove('error')
    }else{
        nom.classList.add('error')
    }
}

function validarconfirmacion(){
    var cont1=document.querySelector('#contrasema');
    var cont2=document.querySelector('#contarsenas');
    if(cont1.value==cont2.value){
        cont2.classList.remove('error')
        }else{
            cont2.classList.add('error')
        }
}

function validarbusca() {
    var dato = document.querySelector('#buscar,#buscao');
    if (dato.value.length > 0 && dato.value.length <5) {
        dato.classList.remove("error");
    } else {
        dato.classList.add("error")
    }
}