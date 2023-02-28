setInterval(showTime, 1000);
function showTime() {
    let time = new Date();
    let hour = time.getHours();
    let min = time.getMinutes();
    let sec = time.getSeconds();
    am_pm = "صبح";
  
    if (hour > 12) {
        hour -= 12;
        am_pm = "عصر";
    }
    if (hour == 0) {
        hr = 12;
        am_pm = "صبح";
    }
  
    hour = hour < 10 ? "0" + hour : hour;
    min = min < 10 ? "0" + min : min;
    sec = sec < 10 ? "0" + sec : sec;
  
    let currentTime = hour + ":" 
            + min + ":" + sec + " "+am_pm;
  
    document.getElementById("clock")
            .innerHTML = currentTime;
}
showTime();


$('.carousel').carousel({
    interval: 2000
  })