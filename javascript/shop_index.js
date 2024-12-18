import { Good, GoodsList, Basket } from "./shop_v2.js";

const data = [
    [1, "Ботинки Саламандра", "Очень качественная обувь", [39, 40, 41, 43, 44, 45], 3490, true],
    [2, "Рубашка", "Удобная рубашка для костюма", ["S", "M", "L", "XXL", "XXXL"], 770, true],
    [3, "Брюки черные", "Элегантные брюки на лубой случай", ["S", "M", "L", "XXL", "XXXL"], 1090, true],
    [4, "Ботинки Ральф", "№1 для состоятельных граждан", [41, 42, 43, 44, 45, 46], 5990, true],
    [5, "Костюм спортивный синий", "Для походов в горы", ["M", "L", "XL", "XXL"], 2790, true],
    [6, "Костюм спортивный розовый", "Для стройных дам", ["XS", "S", "M", "L"], 2290, true],
    [7, "Костюм спортивный детский", "Для самых маленьких", [96, 104, 113, 127, 136], 1490, true],
    [8, "Кроссовки спортивные", "Для всей семьи", [27, 31, 33, 37, 39, 41, 42, 43, 45, 46, 47, 48], 3190, true],
];

const goodsList = new GoodsList();
const goods = [];

data.forEach((params,index) => {
    const [id] = params;
    const good = new Good(...params);
    if (id > 1 && id <=5 && id % 2 > 0) {
        good.setAvailable(false);
    }
    //console.log(good)
    goodsList.add(good);
    goods.push(good);

})

//console.log(goodsList.list);

goodsList.filter = /спорт/i;
console.log("---------после примения фильтра----------");
//console.log(goodsList.list);

//goodsList.sortPrice = true;
//goodsList.sortDir = false;

//console.log(goodsList.list);


const basket = new Basket();
const boots = goods.find((good) => good.id === 4);
const shirt = goods.find((good) => good.id === 2);
const pant =  goods.find((good) => good.id === 3);
//console.log(basket.goods)
//console.log(boots)

basket.add(boots, 5);
basket.add(shirt, 1);
basket.add(pant, 1);
console.log(basket.goods)

//console.log("Общее количество:", basket.totalAmount);

// console.log("--------------------");
// console.log("Вообще и одной пары ботинок хватит");

//basket.remove(boots, 4);
//basket.clear();

//проверить корзину после добавления существующих товаров.
// basket.add(pant, 10);
// basket.add(pant, 2);
// basket.remove(pant, 15);

// console.log("--------------------");
// console.log(basket.goods)
// console.log("Общее количество:", basket.totalAmount);
// console.log("Общее cумма корзины:", basket.totalSumm);

// const order = basket.goods.find((item) => item.id === shirt.id);
// console.log(order)
// order.setAvailable(false);


//basket.removeUnavailable();
// console.log("---------В КОРЗИНЕ СЕЙЧАС-----------");
// console.log(basket.goods)