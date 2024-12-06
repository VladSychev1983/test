function createCatalog() {
        let catalog = {
         goods:[],
         addGood: function (id, name, description, sizes, price, available) { 
             //create good here
             objGood = {id:id, name:name, description:description, sizes:sizes, price:price, available:available}
             this.goods.push(objGood);
         },
         getGood: function (id) { 
             //search good here
            for (const element of this.goods) {
                if (element["id"] === id) {
                return element;
                }
            }
            return "null"; 
        } 
    }
return catalog;
}

function createCart() {
    let cart = {
        orders:[],
        addGood: function(obj) {
            //add good  { good: link, amount: quantity}
            this.orders.push(obj);
        },
        removeGood: function(id) {
            //remove good
            let counter = -1;
            for (const element of cart.orders) {
                counter++;
                if (element["good"].id === id) {
                this.orders.splice(counter, 1);
                }
            }
        },
        clearCart: function() {
          this.orders = [];
        },
        getTotalAmountAndTotalSumm: function() {
            let totalAmount = 0;
            let totalSumm = 0;
            for (let index = 0; index < this.orders.length; index++) {
                const element = this.orders[index];
                totalAmount += element["amount"];
                totalSumm += element["good"].price * element["amount"];  
           }     
            return {totalAmount:totalAmount, totalSumm:totalSumm};
        }
    }
    return cart;
}

//каталог
let catalog = createCatalog();
catalog.addGood(1,"Рубашка белая", "Стильная", ["XS","S"], 49, true);
catalog.addGood(2,"Бутылка пива", "Вкусная", ["0.5"], 100, true);
catalog.addGood(3,"Кожанная куртка", "Версачи", ["XXL"], 3500, true);
catalog.addGood(4,"Майка", "Фуйка", ["XXL"], 500, true);
//console.log(catalog.getGood(1));
//console.log(catalog.goods);

//корзина
let cart = createCart();
cart.addGood({good: catalog.getGood(1), amount: 2});
cart.addGood({good: catalog.getGood(2), amount: 5});
cart.addGood({good: catalog.getGood(3), amount: 5});
//console.log(cart.orders);

//cart.removeGood(2);
console.log(cart.orders);
console.log(cart.getTotalAmountAndTotalSumm())
// console.log(cart.clearCart())
// console.log(cart.orders);

/* это у нас добавляется в корзину в тренражере.
{
  good: {
    id: 3,
    name: 'Ботинки Саламандра',
    description: 'Без них не обойтись в плохую погоду',
    size: [ 39, 41, 42, 43, 45, 46 ],
    price: 19,
    available: false
  },
  amount: 1
}

{
  good: {
    id: 4,
    name: 'Кроссовки спортивные',
    description: 'Лучшие для бега',
    size: [ 37, 38, 39, 41, 44, 45 ],
    price: 4.9,
    available: true
  },
  amount: 1
}
*/
