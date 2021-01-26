let slider=document.getElementById('slider');
let img=document.querySelectorAll("#slider img")
let button=document.querySelectorAll('button')
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
    let leftIndex=0
    if(buttonId=='right'){
        for(let i=0;i<img.length;i++){
            if(leftIndex<img.length*slider.offsetWidth){
                leftIndex-=img[i].offsetWidth;
                img[i].style.left=leftIndex+'px'
                
            }
        
        }
    }
    else{
       for(let i=0;i<img.length;i++){
                if(leftIndex>0){
                    leftIndex+=img[i].offsetWidth;
                    
                    img[i].style.left=leftIndex+'px'
                    
                }
            
        }
        
    }
}