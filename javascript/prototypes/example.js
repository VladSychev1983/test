function createProduct (id,price, name, category) {
    this.id = id;
    this.price = price;
    this.name = name;
    this.category = category;
    //new method inside constructor (this variant wastes your memory!!)
    this.getInfoConstructor  = function() {
         return `${category} - ${price}`;
     }
}

//create method inside prototype (this variant saves your memory.!!)
createProduct.prototype.getInfo  = function(additional) {
    return `${this.category} - ${this.price} - ${additional}`;
}
const tshirt = new createProduct(280, 340,'No name t-shirt','closes');

const person = {
    name:  'john',
    age: 45
};

//toString() is inside prototypes
console.log(person.toString());
console.log(tshirt.getInfoConstructor());
console.log(tshirt.getInfo());

//check tshirt belons to createProduct
console.log(tshirt instanceof createProduct);

//borrow method.
const getInfo = tshirt.getInfo;
console.log(getInfo()); // here no context bind that's why undefined - undefined as result;

const ctx = {
    category: 'Toys',
    price: 4000
}

console.log(getInfo.call(ctx, 'some text'));

//apply example
console.log(getInfo.apply(ctx, ['some args']))

//find max number in array.
const data = [1,20,234,343,22,123];
console.log(Math.max(...data));
console.log(Math.max.apply(null, data));

//bind example
function add (a,b) {
    return a + b;
}
const add10 = add.bind(null, 10);
console.log(add10(8))


function add_new (a,b) {
    return this.value + a + b;
}
const add2 = add_new.bind ({
    value: 10
}, 5)
console.log(add2(9));

