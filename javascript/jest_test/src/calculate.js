export function calculateTotal(purchases) {
    let result = 0;
    for (let i = 0; i < purchases.length; i++) {
        result += purchases[i].count * purchases[i].price;
    }
    return result;
}

// commonjs standart
//module.exports = {
//    calculateTotal
//};

