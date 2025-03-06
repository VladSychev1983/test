// TODO: write your code here
import sum from './basic.js';
import orderByProps from './char_sort.js';

console.log('worked');

console.log(sum([1, 2]));

const obj = {name: 'мечник', health: 10, level: 2, attack: 80, defence: 40};
const res = orderByProps(obj, ["name", "level"]);
console.log(res);