let userName = "Изя";
console.log(userName);
// циклы
let numbers = [123,15,34,33,3533,33434,99];

for (let index = 0; index < numbers.length; index++) {
    const element = numbers[index];
    console.log(element)
    
}

let idx = 10;
while(idx > 0) {
console.log(idx);
idx--;
}

// выполняет do 1 раз а потом проверяет нужны ли еще итерации. 
let idx1 = -10;
do {
console.log(idx1);
idx1--;
} while(idx1 > 0)


for (const number of numbers) {
   console.log(number);
}

// forin перебрать свойства и значения объекта.
let users = {
    name: "имя пользователя",
    age: 30,
    gender: "мужской",
    height: 170,
}

for (const user in users) {
    if (Object.prototype.hasOwnProperty.call(users, user)) {
        const value = users[user];
        console.log(user, value)        
    }
}

//функции.
//классичиский (classic)
function sum(a,b) {
    return a+b;
}

// функциональное выражение. (function expression)
const sum2 = function (a,b) {
    return a+b;
}

//Стрелочная функция 
const a = (a,b) => {}

// внутри функции доступен псевдомассив arguments[] со всеми аргументами.

// rest оператор  - через c доступны массив переданных аргументов.
function sum3(a,b,...c) {
}

//значение по умолчанию при undefined будет sum
function calc(a,b, operation = 'sum') {

}

//рекурсия - вызов функции самой себя .
// явная - вызывает саму себя
// неявная - вызывает функцию которая в последующем вызовет эту же функцию.
//функция вычисления факториала через рекурсию.

function factorial(n) {
    if (n === 1) {
        return 1;
    }
    return n * factorial(n-1);
}

// вычисление чисел фибонначи.
function fibo(n) {
    if(n < 2) {
        return n;
    }
    return fibo(n-1) + fibo(n-2);
}

console.log(fibo(2));
console.log(fibo(3));
console.log(fibo(4));
console.log(fibo(5));
console.log(fibo(6));

//objects
(1).toString();
"HELLO".toLowerCase();
//read
let client1 = {};
let client2 = {};
client1.name = client2['name'];
//add
client1.postition = 'CEO';
//delete
delete client1.postition;

//methods of object valriabe "this"
client1.setPosition = function (postition) {
    this.postition = postition;
};
client1.setPosition('CEO');

//goods
const goods = [
    { name: "Апельсины", price: 70, id: 1},
    { name: "Фейхоа", price: 1000, id: 2},
    { name: "Кофе", price: 300, id: 3},
    { name: "Мандарины", price: 190, id: 4},
    { name: "Лук", price: 20, id: 5},
    { name: "Морковь", price: 170, id: 6},
]
console.log(goods);
console.log(goods[0]);
console.log(goods[1]);


const card = [
    { good: goods[1],
      count: 3  
    },
    {  good: goods[2],
        count: 2
    },
]

goods[0].name = "Апельсины Абхазия";
console.log(goods[0]);
console.log(card);

//count goods in card.
let sum_card = 0;
for (const goodInCard of card) {
   sum_card += goodInCard.good.price *  goodInCard.count;
}
console.log('Стоимость товаров:',  sum_card);