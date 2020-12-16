let textid=document.getElementById('text');
let togglebuttonid=document.getElementById('togglebutton');
let alertpid=document.getElementById('alertp');
let submitbuttonid=document.getElementById('submit');
let type=false
submitbuttonid.addEventListener('click',()=>{
    write()
})

togglebuttonid.addEventListener('click',()=>{
    showhide()
})

function write(){
  
    if(textid.value==''){
        alertpid.innerHTML='Xais olunur bos yerleri doldurasiniz';

    }
    else{
        alertpid.innerHTML=textid.value
    }
}

function showhide(){
    if(type==false){
        textid.type='text';
        type=true
        togglebuttonid.innerHTML='Hide';
    }
    else{
        textid.type='password';
        type=false
        togglebuttonid.innerHTML='Show';
    }
}