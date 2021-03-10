let lightbox=document.getElementById('lightbox');// lightbox

let innerlightbox=document.getElementById('inner-lightbox-2');// Inner lightbox


let portfolioItem=document.getElementsByClassName('row-item') //Portfolio Item

let closeLightbox=document.getElementById('closer-button'); // close button for lightbox

let slider=document.getElementById('slider')

let sliderImg=document.getElementsByClassName('slider-img')

let sliderButton=document.getElementsByClassName('sliderbut')

let data=0

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



// Function for Modal

function openModal(itemValue){
    
    lightbox.style.width='100%';
    lightbox.style.opacity='100%';
    
  
    innerlightbox.firstElementChild.nextElementSibling.innerHTML=itemValue.firstElementChild.nextElementSibling.firstElementChild.innerHTML



              
           
}

function closeModal(){
    lightbox.style.width='0%';
    lightbox.style.opacity='0%';
    data=0
    for(let i=0;i<sliderImg.length;i++){

        sliderImg[i].style.left='0px';
    }
}

// function for lightbox slider


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