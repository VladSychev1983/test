// TODO: write your code here
import sum from './basic.js';
//import Character, { Bowerman } from './character.js';
import Character, { Bowerman } from './character.js';

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

const char3 = new Bowerman ('Myname', 'Bowman', '100', '50', '30', '70');
console.log(char3);