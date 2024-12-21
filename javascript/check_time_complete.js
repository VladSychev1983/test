//замеряем время исполнения программы.

export const trace = function (count) {

    function fib(n) {
      return n <= 1 ? n : fib(n - 1) + fib(n - 2);
    }
  
    const startTime = Date.now();
    let duration = 0;
      try {
    fib(count);
      }
      catch(error) {
          }
      finally {
    duration = Date.now() - startTime;
      }
    return duration;
  };


let duration = trace(8);
console.log(`Время выполнения составило ${duration} милисекунд`); // Ожидаем что время выполнения будет не больше 10-ти ms

duration = trace(37);
console.log(`Время выполнения составило ${duration} милисекунд`); // Ожидаем что время выполнения будет не меньше 100-та ms

duration = trace(41);
console.log(`Время выполнения составило ${duration} милисекунд`); // Ожидаем что время выполнения будет больше секунды (1000 ms)

duration = trace(15000);
console.log(`Время выполнения составило ${duration} милисекунд`); // Ожидаем что время выполнения будет не больше 10-ти ms