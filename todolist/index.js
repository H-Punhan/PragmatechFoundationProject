let addbutton=document.getElementById('add-button')
let text=document.getElementById('text')
let deletebutton=document.getElementById('delete-button')

addbutton.addEventListener('click',()=>{
   document.getElementById('todo-div').innerHTML+="<div id='text-div'><input type='checkbox' class='check'><p>"+text.value+"</p></div>";
})
