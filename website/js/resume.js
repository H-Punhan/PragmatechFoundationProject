


let skills=[

    {lang:'Html/css',
     level:'90%'
    },
    {lang:'Javascript',
     level:'85%'
    },
    {lang:'Python',
     level:'0%'
    },
    {lang:'Sql',
     level:'0%'
    }
    ,{lang:'Php',
    level:'40%'
   }

]


for(let i=0;i<skills.length;i++){
    
    document.getElementById('resume-div-skills-row').innerHTML+=`
    <div class="col12" id='skill-bar-text'>
        <h5>${skills[i].lang}</h5>
        <p>${skills[i].level}</p>
    </div>
    <div class="col12 skill-bar-bar";>
        <div class="box " style="height:100%;width:${skills[i].level};">

        </div>  

    </div>
    </br>
    `;
   

   
}