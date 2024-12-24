let text = document.getElementById("main");
//достать текст из тега.
console.log(text.textContent)
//поиск элемента по классу. возвращает список.
let text1 = document.getElementsByClassName("mytext")[0]
console.log(text1.textContent)
//свойство class
console.log(text1.className)
//получаем доступ к свойствам картинки.
let myimg = document.getElementById("img");
//let imgsrc = myimg.src;
console.log(myimg.src,myimg.width,myimg.height)

var years = prompt('Сколько вам лет?', 100);
alert('Вам ' + years + ' лет!')