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
