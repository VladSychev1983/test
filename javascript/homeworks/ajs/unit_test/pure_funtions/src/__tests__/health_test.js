import check_health  from "../check_health";
test('check wounded test', () => {
    let obj = {name: 'Маг', health: 30};
    const result = check_health(obj);
    expect(result).toBe('wounded');
});
test('check healthy test', () => {
    let obj = {name: 'Рыцарь', health: 90};
    const result = check_health(obj);
    expect(result).toBe('healthy');
});

test('check critical test', () => {
    let obj = {name: 'Король', health: 10};
    const result = check_health(obj);
    expect(result).toBe('critical');
});
