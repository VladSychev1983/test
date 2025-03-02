// TODO: write your code here
import sum from './basic.js';
import Character, { Bowman } from './character_v2.js';

console.log('worked');

console.log(sum([1, 2]));

const char = new Character('Myname', 'Bowman', '100', '50', '30', '70');
const char2 = new Character('Myname2', 'Zombie', '10', '1', '30', '70');
console.log(char);
console.log(char2);
//check level up
char2.levelUp();
console.log(char2);
// //check damage
char.damage(10);
console.log(char);

const char3 = new Bowman('Myname3', 'Bowman', '100', '50', '30', '70');
console.log(char3);

//incorrect object. must be throw err;
const char4 = new Bowman('Bestbow', 'sometype', '100', '50', '30', '70');
console.log(char4);