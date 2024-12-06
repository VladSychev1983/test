// print some text to dev console.
// console.log("какой-то текст");

// print alert message.
// alert("тестовое сообщение!");

// ask user.
// let res = confirm("подтвердите действие");
// console.log(res);

//ask for data user.  If cancel than promt_res will be "null"
// let promt_res = prompt("введите ваши данные")
// console.log(promt_res);

// //test game
// const numberToGuess = Math.round(Math.random());
// const userAnswer = +prompt("Введите 0 или 1");
// // if (isNaN(userAnswer) || (userAnswer !== 0 && userAnswer !== 1)) {
// // includes проверяет в массиве значение если есть то true нет false
// if (isNaN(userAnswer) || (![0, 1].includes(userAnswer))) {          
//     console.log("Вы ввели не число 1 или 0!");
// }
// else if (userAnswer === numberToGuess) {
//     console.log('Вы угадали!');
// }
// else {
//     console.log('Вы не угадали!');
// }

// let a = -3,
//     b = 45;
// //algorithm euclid
// //большее число делим на меньшее.
// //если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
// //если есть остаток, то большее число заменяем на остаток от деления.
// //переходим к пункту 1.
// while (a != 0 & b != 0){
//     if(a > b){//если а больше б, то а присваиваем а/б
//         a = a % b;
//     }
//     else{
//         b = b % a;//наоборот
//     }
// }

// console.log(a+b);


let a = -3, b = 45;
a = Math.abs(parseInt(a));
b = Math.abs(parseInt(b));
  
// if (isNaN(a) || isNaN(b)) {
//   return NaN;
// }
while (b > 0) {
  [a, b] = [b, a % b];
}

console.log(a);