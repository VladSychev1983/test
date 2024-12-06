export const findPrimeNums = function (amount) {
    let MyArray = [];
    for (let i = 2; i <= amount; i++) {
        if (checkPrime(i)) {
          MyArray.push(i);
          }
    }
    function checkPrime(n) {
        if (n < 2) {
        return false;    
        }
        for (let index = 2; index < n; index++) {
            if (n % index == 0 ) {
                return false;
                }
        }
        return true;
    }

    return MyArray;
  
};

let primeNums = findPrimeNums(1);
console.log(primeNums);



function isPrime(n) {
    // Corner case
    if (n <= 1)
      return false;
  
    // Check from 2 to n-1
    for (let i = 2; i < n; i++)
      if (n % i == 0)
        return false;
  
    return true;
  }
  
  // Driver Code
  
let result = isPrime(4)
console.log(result)


export const findPrimes = function (amount) {
  let MyArray = [];
  let counter = 1;
  while (amount > MyArray.length) {
    counter++;
    if (checkPrime(counter)) {
      MyArray.push(counter);
      }
  }

  function checkPrime(n) {
    if (n < 2) {
    return false;    
    }
    for (let index = 2; index < n; index++) {
        if (n % index == 0 ) {
            return false;
            }
    }
    return true;
  }
  return MyArray;
}
let primeMy = findPrimes(50);
console.log(primeMy);
primeMy = findPrimes(2);
console.log(primeMy);
primeMy = findPrimes(5);
console.log(primeMy);