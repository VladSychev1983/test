const reverseNum = function (num) {
    let result = 0;
  
    while (num > 0) {
        result =  num % 10;
      //result = result * 10 + num % 10;
        //console.log(result)
      num = parseInt(num / 10);
    }
  
    return result;
  };

let result = reverseNum(123);

console.log(result);

result = reverseNum(720);
console.log(result);

result = reverseNum(3);
console.log(result);


result = reverseNum(-33);
console.log(result);