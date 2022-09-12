var mX = -1, mY = -1, lX = -1, lY = -1;
var canvas, ctx;

canvas();
function myFunction() {

}

function draw(){

    if (mX!=-1 && mY!=-1){

        if (lX == -1 && lY == -1){
            //ctx.moveTo(mX, mY);
            //ctx.beginPath();
            lX = mX;
            lY = mY;
        } else {
            if (lX != mX && lY != mY){
                ctx.beginPath();
                ctx.moveTo(lX, lY);
                ctx.lineTo(mX, mY);
                ctx.closePath();
                ctx.stroke();
                //ctx.fillRect(mX, mY, 5, 5);
                console.log("" + mX + 'x' + mY);
                lX = mX;
                lY = mY;
            }
        }
        //lX = mX;
        //lY = mY;

    }
}

function canvas(){
    canvas = document.getElementById("draw");
    ctx = canvas.getContext("2d");
    //ctx.beginPath();
    canvas.addEventListener('mouseup', function (e) {
        mX = e.pageX - e.target.offsetLeft,
        mY = e.pageY - e.target.offsetTop
    });

    //ctx.lineWidth = 5; // толщина линии
    ctx.fillRect(1, 1, 498, 498);
    //ctx.strokeRect(1, 1, 498, 498);
    ctx.strokeStyle = "green";
    ctx.fillStyle = "orange";
    //ctx.font = "24px serif";
    //ctx.strokeText("Hello", 10, 100);

    setInterval(draw, 5);
}