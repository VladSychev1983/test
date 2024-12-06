export const createPerson = function (name, age, gender, mail) {
let person = new  Object();
person = {};

person["name"] = name;
person["age"] = age;
person["gender"] = gender;
person["e-mail"] = mail;
person["sayHi"] = function() { console.log(`Привет! Меня зовут ${this.name}. Буду ${this.gender === 'жен' ? "рада" : "рад"} пообщаться по почте. Пиши мне на ${this["e-mail"]}`)}
return person;
}

let person = createPerson("Родион", 27, "муж", "somebox@mail.ru");
//console.log(person);
//console.log(person.name)
person.sayHi()

console.log(person);
person = createPerson("Анастасия", 21, "жен", "cutebox@ya.ru");
//console.log(person);
//console.log(person.name)
person.sayHi()
console.log(person);



var myObj = new Object(),
  str = "myString",
  rand = Math.random(),
  obj = new Object();

myObj.type = "Dot syntax";
myObj["date created"] = "String with space";
myObj[str] = "String value";
myObj[rand] = "Random Number";
myObj[obj] = "Object";
myObj[""] = "Even an empty string";

// console.log(myObj);