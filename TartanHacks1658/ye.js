
var i;
var userName = "";
var len;

var modal = document.getElementById('id01');

function p(){
    i++;
    if (i < 11 ){
        setTimeout(p,200);
    }
}
function setup() {
    createCanvas(screen.width, screen.height);
    len = 0;
}

function draw() {
    background(220);
    let s = userName + "_";
    textSize(25);
    text(s,150,200);
}

function keyTyped(){
    if (keyCode === BACKSPACE && len > 0){
        userName = userName.substring(0,len-1);
        len--;
    }else{
        len++;
        userName += key;
    }
}