export default function sum(items) {
    let result = 0;
    for (let i = 0; i < items.length; i++ ) {
        result += items[i];
    }      
    return result;
}

