// TODO: write your code here
import sum from './basic.js';
import specialAttack from './attack.js';

const character = {
    name: 'Лучник',
    type: 'Bowman',
    health: 50,
    level: 3,
    attack: 40,
    defence: 10,
    special: [
        {
            id: 8,
            name: 'Двойной выстрел',
            icon: 'http://...',
            description: 'Двойной выстрел наносит двойной урон'
        }, 
        {
            id: 9,
            name: 'Нокаутирующий удар',
            icon: 'http://...'
        // <- обратите внимание, описание "засекречено"
        }
    ]	
};

console.log('worked');

console.log(sum([1, 2]));

const res = specialAttack(character);
console.log(res);
