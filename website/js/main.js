//All Variables

let isOpen=false; // For searchbar

let isOpenMenu=false;   // For mobile menu

let firstSearchbar=document.getElementById('search-bar') // Search bar

let secondSearchbar=document.getElementById('search-bar-2') //Inner SearchBar

let searchBarbutton=document.getElementById('search-bar-open-button') //Button For Search bar

let menuButton=document.getElementById('responsive-menu-button') //Button  for mobile  menu

let responsiveMenu=document.getElementById('responsive-menu') //Mobile menu




// Adding Events 



searchBarbutton.addEventListener('click',()=>{

    openSearcbar()

})

menuButton.addEventListener('click',()=>{

    openMenu()

})




// Functions

// Function for Sesarchbar
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
        searchBarbutton.firstElementChild.className='fas fa-list';
        
        isOpen=false
    }
    

}


// Function for mobile menu
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

