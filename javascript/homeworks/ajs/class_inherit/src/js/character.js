export default class Character {
    constructor (name, type, health, level, attack, defence) {
        this.name = name;
        this.type = type;
        this.health = health;
        this.level = level;
        this.attack = attack;
        this.defince = defence;
        let typesList = [
            'Bowman', 
            'Swordsman', 
            'Magician', 
            'Daemon', 
            'Undead', 
            'Zombie'
        ];
        console.log(typesList);
        if (!typesList.includes(type)) {
            throw new Error(`No type ${type} in typesList`);
        }
        if (typeof name !== 'string' || (name.lenght < 2 || name.length > 10)) {
            throw new Error(`Incorrect name ${name}`);
        }
        this.level = 1;
        this.health = 100;
        switch (type) {
        case 'Bowman':
            this.attack = 25;
            this.defence = 25;
            break;
        case 'Swordsman':
            this.attack = 40;
            this.defence = 10;
            break;
        case 'Magician':
            this.attack = 10;
            this.defence = 40;
            break;
        case 'Undead':
            this.attack = 25;
            this.defence = 25;
            break;
        case 'Zombie':
            this.attack = 40;
            this.defence = 10;
            break;
        case 'Daemon': 
            this.attack = 10;
            this.defence = 40;
            break;
        }
    }
}

export class Bowerman extends Character {

}

export class Swordsman extends Character {

}

export class Magician extends Character {

}

export class Daemon extends Character {

}

export class Undead extends Character {

}

export class Zombie extends Character {

}