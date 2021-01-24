// variables
let isOpen=false;

let responsive_button=document.getElementById('responsive-menu-button');

let responsive_menu=document.getElementById('responsive-menu');




let img=document.getElementById('img')
let imgx=0;
let imgy=0;

//  a links for page change
let navbarIcon=document.querySelectorAll('#navbar-nav-icons a');
let responsivemenuIcon=document.querySelectorAll('#responsive-menu-links a')
let postIcon=document.querySelectorAll('#blog-div-posts a')
let changeArrrows=document.querySelectorAll("#navbar-nav-arrows a")
// all page classes
let changePagediv=document.querySelectorAll('.changePage')
let pageindex=0





// add event to button

responsive_button.addEventListener('click',()=>{

    openMenu();

})

for(let i=0;i<navbarIcon.length;i++){

    navbarIcon[i].addEventListener('click',()=>{
        changePage(navbarIcon[i].id)
    })
    responsivemenuIcon[i].addEventListener('click',()=>{
        changePage(responsivemenuIcon[i].id)
    })
    postIcon[i].addEventListener('click',()=>{
        changePage(postIcon[i].id)
        
        
    })

}

for(let i=0;i<changeArrrows.length;i++){

    changeArrrows[i].addEventListener('click',()=>{
        changePage2(changeArrrows[i])
    })

}

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



// change page 
function changePage(navbarIcona){
    
    

    for(let i=0;i<4;i++){

        if(changePagediv[i].className==navbarIcona+" changePage"){

            changePagediv[i].style.height='100%';
            
            pageindex=i

            navbarIcon[i].style.color='#04B4E0';
           
            
        }
        else{
            changePagediv[i].style.height='0%';
            navbarIcon[i].style.color='black';
            openMenu()
            
          
            

            

        }

    }
}
function changePage2(buttonvalue){
    
    
    
    if(buttonvalue.id=='navbar-arrow-right'){

        
        changePagediv[pageindex].style.height='0%';
        

        pageindex++;

        if(pageindex>3){
            pageindex=0;
        }

        changePagediv[pageindex].style.height='100%';
        
        

    }
        

    else{

        changePagediv[pageindex].style.height='0%';

        pageindex--;

        if(pageindex<0){
            pageindex=3;
        }

        changePagediv[pageindex].style.height='100%';

    }

    for(let i=0;i<navbarIcon.length;i++){

       if(navbarIcon[i] ==navbarIcon[pageindex]){
            navbarIcon[i].style.color="#04B4E0";
       }
       else{
            navbarIcon[i].style.color="black";
       }
       

    }



}