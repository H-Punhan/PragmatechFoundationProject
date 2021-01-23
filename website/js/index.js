// variables
let isOpen=false;

let responsive_button=document.getElementById('responsive-menu-button');

let responsive_menu=document.getElementById('responsive-menu');


let img=document.getElementById('img')
let imgx=0;
let imgy=0;




// add event to button

responsive_button.addEventListener('click',()=>{

    openMenu();

})

// functions
// responsive menu function
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



//  img effect function 
// window.addEventListener('mousemove',(mouse)=>{
    
//     if(window.innerWidth>1200){

    
//     img.style.backgroundPositionX+=mouse.offsetX;
    
//     console.log(img.style.backgroundPositionX)
    
    
    


//     // if(mouse.offsetX>window.innerWidth/2){
        
//     //     if(imgx<5){
//     //         imgx+=1
//     //         console.log(imgx)
//     //     }

        
        
//     //     img.style.backgroundPositionX=imgx+"px";
        

//     // }

//     // else{
        

//     //     if(imgx>-10){
//     //         imgx-=1
//     //         console.log(imgx)
//     //     }
//     //     img.style.backgroundPositionX=imgx+"px";

//     // }

//     if(mouse.offsetY>window.innerHeight/2){
       
//         if(imgy<10){
//             imgy+=1
//             console.log(imgy)
//         }

        
        
//         img.style.backgroundPositionY=imgy+"px";
        

//     }

//     else{
        
//         if(imgy>-10){
//             imgy-=1
//             console.log(imgy)
//         }
//         img.style.backgroundPositionY=imgy+"px";

//     }
// }
// else{

//     img.style.backgroundPositionY=0+"px";

// }
// })


