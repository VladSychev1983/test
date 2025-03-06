import orderByProps from "../char_sort";

test('sort properties', () => { 
    const obj = {
        name: 'мечник',
        level: 2,
        health: 10,
        attack: 80,
        defence: 40,
    };
    const params = [
        'name',
        'level'
    ];
    const expacted = [
        { key: 'name', value: 'мечник' },
        { key: 'level', value: 2 },
        { key: 'attack', value: 80 },
        { key: 'defence', value: 40 },
        { key: 'health', value: 10 },
    ];
    expect(orderByProps(obj, params)).toEqual(expacted);
});