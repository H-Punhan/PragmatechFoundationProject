// variables
let isOpen=false;

let responsive_button=document.getElementById('responsive-menu-button');

let responsive_menu=document.getElementById('responsive-menu');

// add event to button

responsive_button.addEventListener('click',()=>{

    openMenu();

})

// functions

function openMenu(){
    
    
   
    if (isOpen==false){

        responsive_button.firstChild.className='fas fa-times';
        
        if(window.innerWidth>360 ){
            responsive_menu.style.width='360px';
        }

        if(window.innerWidth<=360 ){
            responsive_menu.style.width='100%';
        }


        isOpen=true;
    }
    else{

        responsive_button.firstChild.className='fas fa-bars';

        responsive_menu.style.width='0%';

        isOpen=false;

    }


}


