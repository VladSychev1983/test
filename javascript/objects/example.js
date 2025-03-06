const person = {
    name: 'vlad',
    age: 42,
    address: {
        street: 'Country side',
        building:'3'
    },
}
const interests = {
    count: 5,
    type: 'football'
}

//извлечение объекта.
console.log(person.age);
console.log(person['age']);

//деструктурзация объекта.
const { age, name } = person;
console.log(age);

//добавление свойства
person.balance = 4343;
person["balance"] = 4444;
console.log(person.balance);

//undefined
console.log(person.firstName);

//удаление свойства. (после удаления undefined)
delete person.balance;
console.log(person.balance);

//проверка существования свойства.
console.log(person.balance === undefined);  //true
console.log('firstName' in person); //false
console.log('name' in person);  //true

//задать значение balance по умолчанию.
const { balance = 10000 } = person;

//вложенные объкты.
const { address: { building } } = person;
console.log(building);
//переименование переменной.
const { address: { building:userBuilding } } = person;
console.log(userBuilding);

//разделение объекта с помощью rest оператора.
const  {address, ...data} = person;
console.log(address, data);

//копирование объекта spread.(поверхностное)
const copyObject = { ...person };
console.log(copyObject);

copyObject.name = 'ivan';
//вложенные объект меняются во всех копиях
// чтобы не менялись надо копировать и вложенные свойства.
person.address = { ... person.address };

copyObject.address.street = 'Victory 25';

console.log(person);
console.log(copyObject);

//объединение объектов.
const merged = { ...person, ...interests };
console.log(merged);

//прототипы объекта.
class Person {
    constructor(name,age) {
        this.name= name;
        this.age = age;
    }
}
//создать объект с new.
const person_ = new Person('Petya','25');
//создать объект через Object.
const person2 = new Object; //{}
person2.name = 'Name';
person2.age = '33';

console.log(person2)

//По цепочке если свойство не найдено будет null.
console.log(person.__proto__.__proto__);
console.log(person_.__proto__.__proto__.__proto__);
console.log(person_.__proto__ === Object.getPrototypeOf(person_));

//прикрипление прототипа объекту. setPrototypeOf или Object.create
const entry = {
    id: 1011
}
console.log(person.__proto__)
Object.setPrototypeOf(person, entry);
console.log(person.__proto__);

const person__ = Object.create(entry);
person__.name = 'Some name';
person__.age = 30;
console.log(person__);
console.log(person__.__proto__);

//все свойства объекта
function PersonFunction(name) {
    this.name = name;
}
PersonFunction.prototype.type = 'human';

const dataNew = new PersonFunction('Ivan');
for (const prop in dataNew) {
    console.log(prop); //name , type
}

//если надо только свойства без прототипа hasOwnPropery .
for (const prop in dataNew) {
    if (dataNew.hasOwnProperty(prop)) {
        console.log(prop);  //name
    }
}
console.log(dataNew.hasOwnProperty('type'));
console.log('type' in dataNew);

//все ключи объекта keys (без прототипа)
console.log(Object.keys(dataNew))

//дескрипторы.
//ставим неизменяемое свойство. configurable - удаление, writable- изменение, enumerable - отображение.
Object.defineProperty(dataNew, 'birthday', {
    value: '1983-05-03',
    writable: false,
    configurable: false,
    enumerable: true
})
console.log(dataNew.birthday);
dataNew.birthday = '03-07-2005';
console.log(dataNew.birthday);

console.log(Object.keys(dataNew));

//setter example

Object.defineProperty(dataNew, 'newHabit', {
    set: function(value) {
        console.log('Попытка устновить новое значение.' + value);
    }
})
dataNew.newHabit = 'somehabit';

//getter example.
Object.defineProperty(dataNew, 'newProperty', {
    get: function() {
        return 'some result from getter!'
    }
});
console.log(dataNew.newProperty);

//получение дескрипторов свойства объекта.
console.log(Object.getOwnPropertyDescriptor(dataNew, 'birthday'));

const data_test = {};
console.log(Object.getOwnPropertyDescriptor(data_test.__proto__, 'toString'));

//ограничения объкта. freeze, seal, preventExtensions
const someObject = {
    name: "Tanya",
    age: 40
}
Object.freeze(someObject);
someObject.age = 10;
someObject.birthday = '1983-05-03';
console.log(someObject.age, someObject.birthday);
console.log(Object.isFrozen(someObject));
//for seal
console.log(Object.isSealed(someObject));
//for preventExtensions
console.log(Object.isExtensible(someObject));