let slider=document.getElementById('slider');
let img=document.querySelectorAll("#slider img")
let button=document.querySelectorAll('button')
let leftIndex=0
for(let i=0;i<img.length;i++){
    img[i].style.width=slider.offsetWidth+'px'
    img[i].style.flexBasis=slider.offsetWidth+'px'

}

for(let i=0;i<button.length;i++){
    button[i].addEventListener('click',()=>{
        changePhoto(button[i].id)
    })
}

function changePhoto(buttonId){
    
    leftIndex=0
    if(buttonId=='right'){
        
        for(let i=0;i<img.length;i++){
            if(leftIndex<=(img.length-1)*slider.offsetWidth){
                
             img[i]
            }
        
        }
       
    }
    else{
       for(let i=0;i<img.length;i++){
                
                    
                    img[i].style.left=img[i].offsetWidth+'px'
                    console.log(img[i].width+"-" +img[i].offsetWidth +" sekilller")
                    console.log(img[i].style.left +'sekilin left deyeri')

                    
                
            
        }
        
    }
    
}