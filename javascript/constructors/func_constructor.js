//Example function constructor.
function createProduct(id, price, name, category) {
    const product = {
        id,
        price,
        name,
        category,
    }
    return product;
}

function createProductNew(id,price, name, category) {
    this.id = id;
    this.price = price;
    this.name = name;
    this.category = category;
    //new method inside constructor
    this.getInfo  = function() {
        return `${category} - ${price}`;
    }
}

const tshirt = createProduct(280, 340,'No name t-shirt');
const tshirt_new = new createProductNew(280, 340,'No name t-shirt');

//add new object 
tshirt_new.discount = 50;

//create new methods in object
// tshirt.getInfo() = function() {
//     return 't-shirt - 340';
// }
// tshirt_new.getInfo() = function() {
//     return 't-shirt - 500';
// }


console.log(tshirt);
console.log(tshirt_new);
