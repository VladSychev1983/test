export const complexCalc = function (count) {
    function fib(n) {
      return n <= 1 ? n : fib(n - 1) + fib(n - 2);
    }
    //запуск функции фиббоначи в асинхронном режиме через promise.

      let resultPromise = new Promise(function (resolve, reject) {
          try {
          const result = fib(count);
          resolve(result);
              }
          catch(error) {
              reject(error);
              }
      });
      return resultPromise.then()
  };

  console.log("Основная логика что-то выполняет здесь");

complexCalc(8).then((result) => console.log(result));

console.log("Основная логика тоже что-то выполняет здесь");

complexCalc(41).then((result) => console.log(result));

console.log("Основная логика опять что-то выполняет здесь");

complexCalc(25000)
  .then((result) => console.log(result))
  .catch((error) => {
    console.log("Произошла ошибка:");
    console.log("Тип ошибки:", error.name);
    console.log("Описание ошибки:", error.message);
  });
