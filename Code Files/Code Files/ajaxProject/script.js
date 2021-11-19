var playerContainer=document.getElementById("player-info");
var btn=document.getElementById("btn");

btn.addEventListener('click',function(){
    var req=new XMLHttpRequest;
    req.open('GET', 'https://raw.githubusercontent.com/UnpredictablePrashant/LearnAdvanceJS/main/players.json');
    
    req.onload=function(){
       // console.log(req.responseText);
    
       var playerInd=JSON.parse(req.responseText);
       console.log(playerInd[0]);
       rendererFun(playerInd)
    }
    req.send();
})

function rendererFun(player){
    var textData="";
    for(i of player){
        textData="<p>" +i.name +" is a " + i.handed +" handed player and is a "+ i.type +"</p>"
        playerContainer.insertAdjacentHTML('beforeend',textData);
    }
}
