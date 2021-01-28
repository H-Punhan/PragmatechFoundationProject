let imgurl=document.getElementById('imgUrl')
let bannerPos=document.getElementById('bannerPos')
let createbtn=document.getElementById('createButton')
let createimg=document.getElementById('creator-img');
let createimgbanner=document.getElementById('creator-img-banner')
let imgtext=document.getElementById('imgText')
let created=document.getElementById('created')

imgurl.addEventListener('keyup',()=>{
    createimg.style.backgroundImage='url('+imgurl.value+')';
    console.log(imgurl.value)
})

imgurl.addEventListener('mouseout',()=>{
    createimg.style.backgroundImage='url('+imgurl.value+')';
    console.log(imgurl.value)
})

bannerPos.addEventListener('change',()=>{
    
    if(bannerPos.value=="0%"){
        createimgbanner.style.top='unset';
        createimgbanner.style.bottom='0%';
    }
    else{
        createimgbanner.style.bottom='unset';
        createimgbanner.style.top='0%';
    }
    
})

imgtext.addEventListener('keyup',()=>{

    createimgbanner.innerHTML=imgtext.value

})

createbtn.addEventListener('click',()=>{
    if(imgurl.value!='' && imgtext.value!=""){
        created.innerHTML=""
       let banner=document.createElement('div')
       let creatorimg=document.createElement('div')
       banner.setAttribute('id','creator-img-banner')
       banner.innerHTML=imgtext.value
       if(bannerPos.value=="0%"){
        banner.style.top='unset';
        banner.style.bottom='0%';
        }
        else{
            banner.style.bottom='unset';
            banner.style.top='0%';
        }
    
    
       creatorimg.setAttribute('id','creator-img')

       creatorimg.style.backgroundImage='url('+imgurl.value+')'
    
       creatorimg.appendChild(banner)
       
       created.appendChild(creatorimg)


        
    }
    else{
        window.alert('Boş yerləri  doldurun')
    }
})

