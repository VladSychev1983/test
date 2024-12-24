const img = document.getElementById("cookie");
let bool = true;
img.onclick = () => {
    if (bool) {
    img.width += 20;
    img.height += 20;
    }
    else {
    img.width -= 20;
    img.height -= 20; 
    }
    const counter = document.getElementById("clicker__counter");
    let count = Number(counter.textContent) + 1;
    counter.textContent = count;
    bool = !bool;
}