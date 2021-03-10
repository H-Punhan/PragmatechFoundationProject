//All Variables

let isOpen=false; // For searchbar

let isOpenMenu=false;   // For mobile menu

let firstSearchbar=document.getElementById('search-bar') // Search bar

let secondSearchbar=document.getElementById('search-bar-2') //Inner SearchBar

let searchBarbutton=document.getElementById('search-bar-open-button') //Button For Search bar

let menuButton=document.getElementById('responsive-menu-button') //Button  for mobile  menu

let responsiveMenu=document.getElementById('responsive-menu') //Mobile menu

let arrowButton=document.getElementsByClassName('arrow')





// Adding Events 


for(let i=0;i<arrowButton.length;i++){
    arrowButton[i].addEventListener('click',()=>{
        changePage(arrowButton[i])
    })
    
}


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


function changePage(a){
    let pages=['index.html','resume.html','portfolio.html','blog.html','contact.html']
    url=window.location.pathname;
    url=url.substring(url.lastIndexOf('/')+1)

    if(a.id=='arrow-right'){
        for(let i=0;i<pages.length;i++){
            if(pages[i]==url){
                console.log(pages[i])
                pages[i]=pages[i+1]
                if(pages[i]==undefined){
                    pages[i]='index.html';
                }
                
                
                window.location.href=pages[i]
                
            }
            
        }
    }
    else{
        for(let i=0;i<pages.length;i++){
            if(pages[i]==url){
                console.log(pages[i])
                pages[i]=pages[i-1]
                if(pages[i]==undefined){
                    pages[i]='contact.html';
                }
                
                
                window.location.href=pages[i]
                
            }
            
        }
    }
    

}

