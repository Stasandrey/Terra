


function myFunction() {
    var id = setInterval(frameTime, 1000);
    document.getElementById("demo").innerHTML = "Start.";
    canvas()
    myMove();
}
function frameTime(){

   var date;
   var h, m, s, hs, ms, ss;
   date = new Date();
   h = date.getHours();
   hs = '' + h;
   if (h < 10) {
       hs = '0' + hs;
   }
   m = date.getMinutes();
   ms = '' + m;
   if (m < 10) {
       ms = '0' + ms;
   }
   s = date.getSeconds();
   ss = '' + s;
   if (s < 10) {
       ss = '0' + ss;
   }
   document.getElementById("time").innerHTML =  hs + ':' + ms + ':' + ss;
   console.log("Ok");
}

function myMove() {
    var elem =  document.getElementById("animate");
    var pos = 0;
    var id = setInterval(frame, 5);
    function frame() {
        if (pos == 350) {
             clearInterval(id);
        } else {
             pos++;
             elem.style.top = pos + 'px';
             elem.style.left = pos + 'px';
        }
     }
}
function canvas(){
    var canvas = document.getElementById("draw");
    console.log(canvas)
    var ctx = canvas.getContext("2d");
    console.log(ctx)
    ctx.lineWidth = 5; // толщина линии
  // x,y,radius,startAngle,endAngle,anticlockwise
    ctx.arc(200,200,75,0, 2*Math.PI,true);
    ctx.stroke();
}