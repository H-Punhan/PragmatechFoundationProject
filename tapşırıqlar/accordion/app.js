let accardion_Item=document.getElementsByClassName("item")
let isOpen=false;

for(let i=0;i<accardion_Item.length;i++){
    accardion_Item[i].firstElementChild.addEventListener('click',()=>{

        openText(accardion_Item[i])

    })
}


function openText(itemData){
    for(let i=0;i<accardion_Item.length;i++){
        if(accardion_Item[i]!=itemData){
            
            accardion_Item[i].firstElementChild.nextElementSibling.style.padding='0px';
            accardion_Item[i].firstElementChild.nextElementSibling.style.height='0px';
            accardion_Item[i].firstElementChild.firstElementChild.nextElementSibling.className='fas fa-arrow-up';
           
            

            
        }
        else{
            
            
            if(accardion_Item[i].firstElementChild.nextElementSibling.style.height=='auto'){
                accardion_Item[i].firstElementChild.nextElementSibling.style.height='0px';
                accardion_Item[i].firstElementChild.nextElementSibling.style.padding='0px';
                accardion_Item[i].firstElementChild.firstElementChild.nextElementSibling.className='fas fa-arrow-up';
            }
            else{
                accardion_Item[i].firstElementChild.nextElementSibling.style.height='auto';
                accardion_Item[i].firstElementChild.nextElementSibling.style.padding='10px';
                accardion_Item[i].firstElementChild.firstElementChild.nextElementSibling.className='fas fa-arrow-down';
            }
            
        }
        
    }
    
    
 

}
