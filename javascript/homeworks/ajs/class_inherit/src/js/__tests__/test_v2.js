import * as Mynameclass from "../character_v2";

test ("check Charecter class", () => {
    const expected = {
        name: 'Myname2',
        type: 'Zombie',
        health: 100,
        level: 1,
        attack: "30",
        defence: "70",
    };
    const result = new Mynameclass.default(
        'Myname2', 'Zombie', '10', '1', '30', '70');
    expect(result).toEqual(expected);
});

test ("check type", () => {
    const result = () => new Mynameclass.default(
        'Myname2',
        'UnknownType',
        '10',
        '1',
        '30',
        '70');
    expect(result).toThrowError('No type UnknownType in typesList');
});

test ("check name 1", () => {
    const result = () => { new Mynameclass.default(
        'M',
        'Zombie',
        '10',
        '1',
        '30',
        '70');
    };
    expect(result).toThrowError("Incorrect name M");
});

test ("check name 11", () => {
    const result = () => new Mynameclass.default(
        'Superlonglogname', 
        'Zombie', 
        '10', 
        '1', 
        '30',
        '70');
    expect(result).toThrowError("Incorrect name Superlonglogname");
});


test ("check levelUp func", () => {
    const expected = 2;

    const obj = new Mynameclass.default(
        'NameN', 
        'Magician', 
        '10', 
        '15', 
        '33', 
        '22');
    obj.levelUp();
    const result = obj.level;    
    expect(result).toEqual(expected);
});

test ("check levelUp health 0", () => {
    const expected = 'this person is dead';
    const obj = new Mynameclass.default(
        'Name', 
        'Undead', 
        '33', 
        '29', 
        '30', 
        '70');
    obj.health = 0;
    //const result = obj.levelUp();
    expect(() => obj.levelUp()).toThrowError(expected);
});

test("damage func", () => {
    const expected = 94;
    const obj = new Mynameclass.default(
        'Name', 
        'Undead', 
        '33', 
        '29', 
        '30', 
        '70');
    obj.damage(20);
    const result = obj.health;
    expect(result).toBe(expected);
});

test("check Bowerman class", () => {
    const expected = {
        name: 'Name',
        type: 'Bowman',
        health: 100,
        level: 1,
        attack: 25,
        defence: 25
    };
    const result = new Mynameclass.Bowman(
        'Name', 
        'Bowman', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test("check Swordsman class", () => {
    const expected = {
        name: 'Name',
        type: 'Swordsman',
        health: 100,
        level: 1,
        attack: 40,
        defence: 10
    };
    const result = new Mynameclass.Swordsman(
        'Name', 
        'Swordsman', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test("check Magician class", () => {
    const expected = {
        name: 'Name',
        type: 'Magician',
        health: 100,
        level: 1,
        attack: 10,
        defence: 40
    };
    const result = new Mynameclass.Magician(
        'Name', 
        'Magician', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test("check Daemon class", () => {
    const expected = {
        name: 'Name',
        type: 'Daemon',
        health: 100,
        level: 1,
        attack: 10,
        defence: 40
    };
    const result = new Mynameclass.Daemon(
        'Name', 
        'Daemon', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test("check Undead class", () => {
    const expected = {
        name: 'Name',
        type: 'Undead',
        health: 100,
        level: 1,
        attack: 25,
        defence: 25
    };
    const result = new Mynameclass.Undead(
        'Name', 
        'Undead', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test("check Zombie class", () => {
    const expected = {
        name: 'Name',
        type: 'Zombie',
        health: 100,
        level: 1,
        attack: 40,
        defence: 10
    };
    const result = new Mynameclass.Zombie(
        'Name', 
        'Zombie', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});