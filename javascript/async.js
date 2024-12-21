
const timeoutResult = setTimeout(() => {
    console.log("из таймаута")
}, 1000);
const intervalResult = setInterval(() => {
    console.log("из интервала")
}, 1000);

console.log(timeoutResult);
console.log(intervalResult);

//остановить выполнение интервала можно функцией clearInterval
//clearInterval(intervalResult);

//Асинхронный вывод массива чисел с помощью Promise
//resolve возвращаем объект список чисел через 5 секунд.

const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("из таймаута");
        resolve([1,2,3,5,10,101]);
    }, 5000);
});
promise.then((numbers) => {
    console.log(numbers);
})

//отлавливаем reject.
 const promise2 = new Promise((resolve, reject) => {
     setTimeout(() => {
         console.log("из таймаута");
         reject(new Error("не получилось получить данные."));
     }, 5000);
 });
 promise2.then((numbers) => {
     console.log(numbers);
 }).catch((error) => {
     console.log(error)
 })

//c приминением async await самовызывающейся функции.
// дожидаемся выполнения промиса с помощью async await.
async function test () {
    const result = await new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("из таймаута");
            resolve('какие-то данные');
        }, 5000);
    });
    console.log(result);
};
test();

async function f() {

    let promise = new Promise((resolve, reject) => {
      setTimeout(() => resolve("готово!"), 1000)
    });
  
    let result = await promise; // будет ждать, пока промис не выполнится (*)
  
    alert(result); // "готово!"
  }
  
  f();

  //отлавливаем error с помощью try catch.
  async function test1 () {
    try {
    const result = await new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("из таймаута");
            reject(new Error("Ошибка функции test1!"))
        }, 5000);
    });
    console.log(result);
    } catch (error) {
        console.log(error);

    }
};
test1();