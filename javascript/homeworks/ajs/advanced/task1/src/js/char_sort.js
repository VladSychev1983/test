export default function orderByProps(obj, sortParams) {
    const firstArray = [];
    const secondArray = [];
    for (const x in obj) {
        if (x === sortParams[0]) {
            firstArray.push({ key:x, value:obj[x]});
        }
        else if (x === sortParams[1]) {
            firstArray.push({ key:x, value:obj[x]});
        }
        else {
            secondArray.push({ key:x, value:obj[x]});
        }
    }
    const compareFn = (a, b) => a.key.localeCompare(b.key);
    const sortedArray = secondArray.sort(compareFn);
    const resultArray = [ ...firstArray, ...sortedArray];
    return resultArray;
}