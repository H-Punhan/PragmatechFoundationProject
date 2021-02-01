// Variables

let isOpen=false;
let isOpenMenu=false;
let firstSearchbar=document.getElementById('search-bar')
let secondSearchbar=document.getElementById('search-bar-2')
let searchBarbutton=document.getElementById('search-bar-open-button')
let menuButton=document.getElementById('responsive-menu-button')
let responsiveMenu=document.getElementById('responsive-menu')


// Adding Events 

searchBarbutton.addEventListener('click',()=>{

    openSearcbar()

})

menuButton.addEventListener('click',()=>{

    openMenu()

})

// Functions

function openSearcbar(){
    if(isOpen==false){

        
        secondSearchbar.style.width='90%';
        if(window.innerWidth<=360){
            firstSearchbar.style.width=(window.innerWidth-searchBarbutton.clientWidth)+'px';
        }
        else{
            firstSearchbar.style.width='311px';
        }
        
        
        isOpen=true
        searchBarbutton.firstElementChild.className='fas fa-times'
    }
    else{

        secondSearchbar.style.width='0%';
        firstSearchbar.style.width='0';
        searchBarbutton.firstElementChild.className='fas fa-bars';
        
        isOpen=false
    }
    

}

function openMenu(){
    
    if(isOpenMenu==false){

        
        
        if(window.innerWidth<=360){
            responsiveMenu.style.width='100%';
        }
        else{
            responsiveMenu.style.width='360px';
        }
        
        
        isOpenMenu=true
        menuButton.firstElementChild.className='fas fa-times'
    }
    else{

        
        responsiveMenu.style.width='0';
        menuButton.firstElementChild.className='fas fa-bars';
        
        isOpenMenu=false
    }

}