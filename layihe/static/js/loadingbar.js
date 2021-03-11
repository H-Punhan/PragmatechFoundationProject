let skillbar=document.getElementsByClassName('load-bar');

window.alert('hello')
for(let i=0;i<skillbar.length;i++){
    console.log(skillbar[i])
    skillbar[i].style.width=skillbar[i].parentElement.previousElementSibling.firstElementChild.nextElementSibling.innerHTML
}

