let img=document.querySelectorAll('#about-div-row-img #img');
let xpos=0;
let ypos=0;

window.addEventListener('mousemove',(m)=>{
    changePos(m)
})

function changePos(m){
    // background x position 
    if(m.clientX>window.innerWidth/2){

       
        xpos-=0.5;
        if(xpos<-5){
            xpos=-5;

        }
        
        
        
    
    }

    else{

        xpos+=0.5;
        if(xpos>5){
            xpos=5;

        }
        
        
    }

    // background y position 
    if(m.clientY>window.innerHeight/2){
        ypos-=1;
        if(ypos<-5){
            ypos=-5;

        }
        console.log(ypos)
    
    }

    else{

        ypos+=1;
        if(ypos>5){
            ypos=5;

        }
        
        
    }

    img[0].style.backgroundPositionX=xpos+'px'
    img[0].style.backgroundPositionY=ypos+'px'

 
    

    

}