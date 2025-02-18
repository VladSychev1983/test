//commonjs standart
//const { calculateTotal } = require('../src/calculate.js');
import { calculateTotal } from "../calculate";

test ("basic test", () => {
    const result = 4;
    expect(result).toBe(4);
});

test('calculate sum', () => {
    const list = [
        {
            id:444,
            name: 'book1',
            count: 3,
            price: 400
        },
        {
            id:333,
            name: 'Javascript',
            count: 1,
            price: 1200
        }
    ];

    const result = calculateTotal(list);
    expect(result).toBe(2400)

})