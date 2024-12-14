const numbers = [1,3,100,10,25];
const max = numbers.reduce((number,max) => number > max ? number : max);
console.log(max);