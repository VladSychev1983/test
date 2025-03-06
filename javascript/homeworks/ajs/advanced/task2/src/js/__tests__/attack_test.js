import specialAttack from "../attack";

test('check specialAttack', () => {
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
    const expected = [
        {
            "description": "Двойной выстрел наносит двойной урон",
            "id": 8,
            "name": "Двойной выстрел",
            "icon": "http://..."
        },
        {
            "description": "описание недоступно",
            "id": 9,
            "name": "Нокаутирующий удар",
            "icon": "http://..."
        }];    
    const result = specialAttack(character);
    //console.log(character);
    expect(result).toEqual(expected);
});