let imgindex=1
for(let i=0;i<1;i++){
    
    let section=document.createElement('section')
    section.setAttribute('id','gallery')
    section.style.width='80%';
    section.style.marginLeft='10%';
    document.body.appendChild(section)
   
    for(let i=0;i<1;i++){

        let container=document.createElement('div')
        container.setAttribute('class','container')
        section.appendChild(container)


        for(let i=0;i<2;i++){
            let row=document.createElement('div')
            row.setAttribute('class','row')
            row.style.display='flex';
            row.style.width='100%';
            container.appendChild(row)
           

            for(let i=0;i<3;i++){

                let col=document.createElement('div')
                let image=document.createElement('img')
                col.setAttribute('class','col-4')
                col.style.width='30%';
                col.style.height='200px';
                col.style.padding='10px';
                col.style.boxSizing='border-box';

                image.src="./img/"+imgindex+'.jpg';
                image.style.height='100%';
                image.style.width='100%';
                image.style.objectFit='cover';
                image.style.borderRadius='10px';

                row.appendChild(col)
                col.appendChild(image)


                imgindex++
                


            }
        }

        
    }
}