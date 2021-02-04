//All Variables

let isOpen=false; // For searchbar

let isOpenMenu=false;   // For mobile menu

let firstSearchbar=document.getElementById('search-bar') // Search bar

let secondSearchbar=document.getElementById('search-bar-2') //Inner SearchBar

let searchBarbutton=document.getElementById('search-bar-open-button') //Button For Search bar

let menuButton=document.getElementById('responsive-menu-button') //Button  for mobile  menu

let responsiveMenu=document.getElementById('responsive-menu') //Mobile menu

let lightbox=document.getElementById('lightbox');// lightbox

let innerlightbox=document.getElementById('inner-lightbox-2');// Inner lightbox


let portfolioItem=document.getElementsByClassName('row-item') //Portfolio Item

let closeLightbox=document.getElementById('closer-button'); // close button for lightbox

let slider=document.getElementById('slider')

let sliderImg=document.getElementsByClassName('slider-img')

let sliderButton=document.getElementsByClassName('sliderbut')

let leftValue;

// Adding Events 



searchBarbutton.addEventListener('click',()=>{

    openSearcbar()

})

menuButton.addEventListener('click',()=>{

    openMenu()

})

//  Adding events to Portfolio items
for(let i=0;i<portfolioItem.length;i++){
    portfolioItem[i].addEventListener('click',()=>{
        openModal(portfolioItem[i])
    })
}

closeLightbox.addEventListener('click',()=>{
    closeModal()
})


for(let i=0;i<sliderButton.length;i++){
    sliderButton[i].addEventListener('click',()=>{
        
        slide(sliderButton[i])
        
    })
}



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

// Function for Modal

function openModal(itemValue){
    
    lightbox.style.width='100%';
    lightbox.style.opacity='100%';
    
  
    innerlightbox.firstElementChild.innerHTML=itemValue.firstElementChild.nextElementSibling.firstElementChild.innerHTML
      


              
           
}

function closeModal(){
    lightbox.style.width='0%';
    lightbox.style.opacity='0%';
}

// function for lightbox slider

let data=0
function slide(button){
    
    
    
    if(button.className=='s sliderbut'){
        data=data+slider.clientWidth;
        console.log(data +'sliderin uzunlugu')
        if(data>slider.clientWidth*(sliderImg.length)){
            data=slider.clientWidth*sliderImg.length
            
            
        }
        
        if(data<slider.clientWidth*(sliderImg.length)){
            
            for(let i=0;i<sliderImg.length;i++){
                sliderImg[i].style.left=-data+'px';
            }
        }
        console.log(data)
        
  
    }
    else{
        data-=slider.clientWidth;
        if(data<0){
            data=0
        }
        for(let i=0;i<sliderImg.length;i++){
            sliderImg[i].style.left=-data+'px';
        }
        console.log(data)
    }
    
    

}