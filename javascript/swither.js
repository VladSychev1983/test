let array = []
export const toogle = function () {
    let bool = true;
    array.push(bool);
    array[0] = !bool;
    return array[0];
}

let enabled = toogle();
console.log(enabled)
enabled = toogle()
console.log(enabled)

let arr = [];
let count = 0;

function counting() {
  arr.push(++count);
  console.log(arr);
}

counting()
counting()
counting()



let bool = false;
function inc() {
    return bool = !bool;
}
console.log(inc())
console.log(inc())
console.log(inc())
console.log(inc())