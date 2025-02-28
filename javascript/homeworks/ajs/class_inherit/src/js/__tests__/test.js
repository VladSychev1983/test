import Character, { Bowerman } from "../character";
test ("basic test", () => {
    const result = 4;
    expect(result).toBe(4);
});

test ("create obj zombie", () => {
    const expected = {
        name: 'Test',
        type: 'Zombie',
        health: 100,
        level: 1,
        attack: 40,
        defence: 10
    };
    const result = new Character(
        'Test', 
        'Zombie', 
        '10', 
        '1', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test ("create obj bowman", () => {
    const expected = {
        name: 'TestBowman',
        type: 'Bowman',
        health: 100,
        level: 1,
        attack: 25,
        defence: 25
    };
    const result = new Character(
        'TestBowman', 
        'Bowman', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test ("create obj swordsman", () => {
    const expected = {
        name: 'TestSword',
        type: 'Swordsman',
        health: 100,
        level: 1,
        attack: 40,
        defence: 10
    };
    const result = new Character(
        'TestSword', 
        'Swordsman', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});


test ("create obj magician", () => {
    const expected = {
        name: 'TestMag',
        type: 'Magician',
        health: 100,
        level: 1,
        attack: 10,
        defence: 40
    };
    const result = new Character(
        'TestMag', 
        'Magician', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test ("create obj undead", () => {
    const expected = {
        name: 'TestUnd',
        type: 'Undead',
        health: 100,
        level: 1,
        attack: 25,
        defence: 25
    };
    const result = new Character(
        'TestUnd', 
        'Undead', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});


test ("create obj daemon", () => {
    const expected = {
        name: 'Dem',
        type: 'Daemon',
        health: 100,
        level: 1,
        attack: 10,
        defence: 40
    };
    const result = new Character(
        'Dem', 
        'Daemon', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});

test ("create obj name less 2", () => {
    const expected = 'Incorrect name D';
    const result = new Character(
        'D', 
        'Daemon', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toThrowError(expected); 
});

test ("create obj name more 10", () => {
    const expected = 'Incorrect name Dddddddddddd';
    const result = new Character(
        'Dddddddddddd', 
        'Daemon', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toThrowError(expected); 
});

test ("create obj noname type", () => {
    const expected = 'No type Daemoni in typesList';
    const result = new Character(
        'Test', 
        'Daemoni', 
        '22', 
        '29', 
        '30', 
        '70');
    expect(result).toThrowError(expected); 
});

test ("check levelUp function", () => {
    const expected = {
        name: 'NameN',
        type: 'Magician',
        health: 100,
        level: 2,
        attack: 22,
        defence: 88
    };

    const obj = new Character(
        'NameN', 
        'Magician', 
        '10', 
        '15', 
        '33', 
        '22');
    const result = obj.levelUp();
    expect(result).toEqual(expected);
});

test ("check levelUp health 0", () => {
    const expected = 'this person is dead';
    const obj = new Character(
        'Name', 
        'Undead', 
        '33', 
        '29', 
        '30', 
        '70');
    obj.health = 0;
    const result = obj.levelUp();
    expect(result).toThrowError(expected);
});

test("damage func", () => {
    const expected = 85;
    const obj = new Character(
        'Name', 
        'Undead', 
        '33', 
        '29', 
        '30', 
        '70');
    const result = obj.damage(20);
    expect(result.health).toBe(expected);
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
    const result = new Bowerman(
        'Name', 
        'Bowman', 
        '33', 
        '29', 
        '30', 
        '70');
    expect(result).toEqual(expected); 
});