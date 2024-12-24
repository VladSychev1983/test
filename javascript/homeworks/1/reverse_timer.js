let timetag = document.getElementById("time");
let start_num = timetag.textContent;

let myInterval = setInterval(function () {
    let counter = Number(start_num--);
    timetag.textContent = counter;
    if (counter == 0) {
        alert("Вы победили в конкурсе");
        clearInterval(myInterval);
        return;
    }
}, 1000);

