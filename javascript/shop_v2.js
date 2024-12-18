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
        if (this.filter instanceof RegExp) {
            let FilteredResult =this.#goods.filter((good) => (good.available===true)).filter((good) => this.filter.test(good.name))
            if(FilteredResult.length > 0) {
                result = FilteredResult;
            }
            else {
                result = this.#goods.filter((element) => element.available == true);
            }
        } 
        else {
            result=this.#goods.filter((good) => (good.available===true));
        };
        if (this.sortPrice) {
            result.sort((a,b) => (a.price-b.price)* (this.sortDir ? 1 : -1))
        }
        return result;
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
    constructor (good, amount) {
        super(good.id, good.name, good.description, good.sizes, good.price, good.available);
        this.amount = amount;
    }
}

class Basket {
    constructor() {
        this.goods = [];
    }
    
    get totalAmount() {
    let totalAmount = this.goods.reduce((total, object) => total + object.amount, 0);
    return totalAmount;
    }
    get totalSumm() {
    let totalSumm = this.goods.reduce((total, object) => total + (object.price * object.amount), 0);
    return totalSumm;
    }
    add(obj, amount) {
    obj.amount = amount;
    let findex = this.goods.findIndex((good) => good.id === obj.id);
    if (findex > -1) {
        this.goods[findex].amount += amount;
        }
    else {
        //let newgood = new BasketGood(obj.id,obj.name,obj.description,obj.sizes,obj.price,obj.available,obj.amount);
        let newgood = new BasketGood(obj,obj.amount);
        this.goods.push(newgood);
        }
    }
    
    remove(obj, remove_count) {
    for (const good of this.goods) {
        if (obj.id === good.id) {
            if (good.amount > remove_count && remove_count > 0) {
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
    this.goods = [];
    return;
    }
    removeUnavailable() {
    let result = this.goods.filter((good) => good.available == true);
    this.clear();
    this.goods = result;
    return result;
        }    
}

export { Good, GoodsList, BasketGood, Basket };