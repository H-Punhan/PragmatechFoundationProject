let loadbar=document.getElementsByClassName('load-bar')

for(let i=0;i<loadbar.length;i++){
   

    loadbar[i].style.width=loadbar[i].parentElement.previousElementSibling.firstElementChild.nextElementSibling.innerHTML
}
    
