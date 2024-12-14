//console.log(Math.pow(3,3));

export const pow = function (num, exp) {
    if (exp <= 0) {
        return 1;
      }
      return Math.pow(num, exp);
}

console.log(pow(2,3))
console.log(pow(-10,5))
console.log(pow(-3,4))
