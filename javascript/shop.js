class Good {
    constructor (id, name, description, sizes, price, available) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.sizes = sizes;
        this.price = price;
        this.available = available;
    }
    
    setAvailable = (bool) => {
        this.available = bool;
    } 
}

class GoodsList {
    #goods = [];
    constructor () {
        this.filter = null;
        this.sortPrice = false;
        this.sortDir = true;    
    }      

    get list() {
        let result = [];
        let sorted_result = [];
        if (this.filter instanceof RegExp) {
            let myRe = this.filter;
            result = this.#goods.filter((element) => myRe.test(element.name) === true);
            if (this.sortPrice == true && this.sortDir == true) {
                let myObj = []
                 for (const element of result) {
                     myObj.push({
                         id:element.id, 
                         name:element.name, 
                         description:element.description, 
                         sizes:element.sizes, 
                         price:element.price, 
                         available:element.available
                     });
               }
            sorted_result = myObj.sort((a,b) => a.price - b.price);
            return sorted_result;
            }
            else if (this.sortPrice == true && this.sortDir == false) {
                let myObj = []
                for (const element of result) {
                    myObj.push({
                        id:element.id, 
                        name:element.name, 
                        description:element.description, 
                        sizes:element.sizes, 
                        price:element.price, 
                        available:element.available
                    });
            }
            let sorted_result = myObj.sort((a,b) => b.price - a.price);
            return sorted_result;
            }
            else {
            console.log("---#goods--after enable filter");
            console.log("Общая сумма в #goods:", this.#goods.length);
            return result;
            }
        }
        else {
        result = this.#goods.filter((element) => element.available == true);
        return result;     
        }
    }

    add(good) {
        this.#goods.push(good);
    }
    
    remove (id) {
        let found_index = this.#goods.findIndex((good) => good.id === id);
        if (found_index > -1) {
            this.#goods.splice(found_index,1);
        } 
    }
}

class BasketGood extends Good {
    constructor (id, name, description, sizes, price, available, good, amount) {
        super(id, name, description, sizes, price, available);
        this.amount = amount;
        this.good = good;
    }
}

class Basket {
    constructor() {
        this.goods = [];
    }
    
    get totalAmount() {
    //общее количество товаров в корзине.
    let totalAmount = this.goods.reduce((total, object) => total + object.amount, 0);
    return totalAmount;
    }
    get totalSumm() {
    //общая стоимость товаров в корзине.
    let totalSumm = this.goods.reduce((total, object) => total + object.price, 0);
    return totalSumm;
    }
    add(obj, amount) {
    //добавляет в корзину если еще нет в корзине или увеличивает количество товара в корзине.
    let myobj = {
        id: obj.id,
        name: obj.name,
        description: obj.description,
        sizes: obj.sizes,
        price: obj.price,
        available:obj.available,
        amount: amount,
        setAvailable: function(bool) { this.available =  bool}
     }
    let findex = this.goods.findIndex((good) => good.id === obj.id);
    if (findex > -1) {
        this.goods[findex].amount += num;
        }
    else {
        this.goods.push(myobj);
        }
    // obj.amount = num;
    // let findex = this.goods.findIndex((good) => good.id === obj.id);
    // if (findex > -1) {
    //     this.goods[findex].amount += num;
    //     console.log(this.goods[findex].amount)
    // }
    // else {
    //     this.goods.push(new BasketGood(obj,num));
    // }
    }
    
    remove(obj, remove_count) {
    //удаляет товар из корзины (если amount >= количеству в корзине) или уменьшает количество товаров в корзине.
    for (const good of this.goods) {
        if (obj.id === good.id) {
            if (good.amount > remove_count && remove_count > 0) {
            //обновить amount в корзине.
            let new_count = Number(good.amount - remove_count); 
            good.amount = new_count;
            }
            else {
                let found_index = this.goods.findIndex((good) => good.id === obj.id);
                if (found_index > -1) {
                this.goods.splice(found_index, 1);
                } 
            }
        }
    }
    return;
    }
    clear() {
    //удаляем все товары в корзине.
    this.goods = [];
    return;
    }
    removeUnavailable() {
    //удаляет все недоступные товары из корзины.
    let result = this.goods.filter((good) => good.available == true);
    this.clear();
    this.goods = result;
    return result;
        }    
}

export { Good, GoodsList, BasketGood, Basket };