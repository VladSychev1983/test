export default class Character {
    constructor (name, type, health, level, attack, defence) {
        this.name = name;
        this.type = type;
        this.health = health;
        this.level = level;
        this.attack = attack;
        this.defence = defence;
        let typesList = [
            'Bowman', 
            'Swordsman', 
            'Magician', 
            'Daemon', 
            'Undead', 
            'Zombie'
        ];
        
        if (!typesList.includes(type)) {
            const err = () => {
                throw new Error(`No type ${type} in typesList`);
            };
            return err;
        }
        if (typeof this.name !== 'string' || 
            (this.name.length < 2 || this.name.length > 10)) {
            const err = () => {
                throw new Error(`Incorrect name ${name}`);
            };
            return err;
        }
        this.level = 1;
        this.health = 100;
    }

    levelUp() {
        if (this.health > 0) {
            this.level += 1;
            this.attack += this.attack + (this.attack * 0.2);
            this.defence += this.defence + (this.defence * 0.2);
            this.health = 100;
        }
        else {
            const err = () => {
                throw new Error('this person is dead');
            };
            return err;
        }
    }

    damage(points) {
        this.health -=  points * (1 - this.defence /100);
    }
}

export class Bowman extends Character {
    constructor(...args) {
        super(...args);
        this.attack = 25;
        this.defence = 25;
    }
}

export class Swordsman extends Character {
    constructor(...args) {
        super(...args);
        this.attack = 40;
        this.defence = 10;
    }

}

export class Magician extends Character {
    constructor(...args) {
        super(...args);
        this.attack = 10;
        this.defence = 40;
    }
}

export class Daemon extends Character {
    constructor(...args) {
        super(...args);
        this.attack = 10;
        this.defence = 40;
    }
}

export class Undead extends Character {
    constructor(...args) {
        super(...args);
        this.attack = 25;
        this.defence = 25;
    }
}

export class Zombie extends Character {
    constructor(...args) {
        super(...args);
        this.attack = 40;
        this.defence = 10;
    }
}