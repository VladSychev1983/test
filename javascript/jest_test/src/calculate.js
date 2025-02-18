export function calculateTotal(purchases, discount) {
    let result = 0;
    for (let i = 0; i < purchases.length; i++) {
        result += purchases[i].count * purchases[i].price;
    }
    if (discount) {
        return result * 0.5;
    }
    return result;
}

// commonjs standart
//module.exports = {
//    calculateTotal
//};

