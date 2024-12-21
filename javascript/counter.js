//замыкания 2 независимых счетчика.
function counter(initialValue) {
    let counter = initialValue;
    return () => {
        return counter++;
    }
}

let counterResult = counter(0);
console.log(counterResult());
console.log(counterResult());
console.log(counterResult());
console.log(counterResult());
console.log(counterResult());

let otherCounterResult = counter(10);
console.log(otherCounterResult());
console.log(otherCounterResult());
console.log(otherCounterResult());
console.log(otherCounterResult());
console.log(otherCounterResult());

console.log(counterResult());
console.log(counterResult());

//функция переключатель true /false

export const toogle = function () {
      let bool = true;
      const returnBool = () => {
          bool = !bool;
          return bool;
          }
    let result = returnBool();
    return result;
  };

// let myfunc = toogle();
//   console.log(myfunc());
//   console.log(myfunc());
//   console.log(myfunc());
//   console.log(myfunc());
toogle()
toogle()
