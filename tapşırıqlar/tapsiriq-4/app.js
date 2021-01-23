let button=document.getElementsByClassName('button')
let slidebtn=document.querySelectorAll('#slider-paging a')

let imageindex=1;

for(let i=0;i<button.length;i++){
    button[i].addEventListener('click',()=>{
        slider(button[i].id)
    })

   

    
    
}

for(let i=0;i<4;i++){
    slidebtn[i].addEventListener('click',()=>{
        slider2(slidebtn[i])
    })
}





function slider(buttonId){

    if(buttonId=='right'){
        
        document.getElementById('sekil-'+imageindex).style.width='0%';
        document.getElementById('p'+imageindex).className='nactive';
        imageindex++;
      
        if(imageindex>4){
            imageindex=1
        }
        
        document.getElementById('sekil-'+imageindex).style.width='100%';
        document.getElementById('description').innerHTML=document.getElementById('sekil-'+imageindex).className;
        document.getElementById('p'+imageindex).className='active';

    }

    if(buttonId=='left'){
        document.getElementById('sekil-'+imageindex).style.width='0px'
        document.getElementById('p'+imageindex).className='nactive'
        imageindex--;
     
        if(imageindex<1){
            imageindex=4
        }
        document.getElementById('sekil-'+imageindex).style.width='100%';
        document.getElementById('description').innerHTML=document.getElementById('sekil-'+imageindex).className;
        document.getElementById('p'+imageindex).className='active'
        

    }

}

function slider2(btnvalue){
    

    document.getElementById('sekil-'+imageindex).style.width='0%';
    document.getElementById('p'+imageindex).className='nactive';
    
   
  
    
    
    document.getElementById('sekil-'+btnvalue.id.slice(1,2)).style.width='100%';
    document.getElementById('description').innerHTML=document.getElementById('sekil-'+btnvalue.id.slice(1,2)).className;
    document.getElementById('p'+btnvalue.id.slice(1,2)).className='active';

    imageindex=btnvalue.id.slice(1,2)
}