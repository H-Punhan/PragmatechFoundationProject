let skillDiv=document.getElementById('skills-div');

let data=[
    
    {
        name:'Css',
        level:'90%'

    },
    {
        name:'Javascript',
        level:'85%'

    },
    {
        name:'Sql',
        level:'80%'

    }
    ,{
        name:'Python',
        level:'80%'

    }
];

for(let i=0;i<data.length;i++){
    document.getElementById('skills-div').innerHTML+=`
    <div id='skill-bar'>
                
                                    <div id='skill-bar-text'>
                                        <h4>${data[i].name}</h4>
                                        <p>${data[i].level}</p>
                                    </div>
                                    <div id='skill-bar-bar'>
                                        <div id='inner-skill-bar-bar' style='width:${data[i].level}'></div>
                                    </div>
                                    
                
                                </div>
    `;
    
}