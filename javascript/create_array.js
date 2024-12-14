/* Создаём массив из 100 полей, 25 из которых случайно заполняем бомбами */
const randomLine = Array(25).fill('bomb').concat(Array(75)).fill('empty',25,100).sort(() => Math.random() - 0.5);
console.log(randomLine);