import calculateCashback  from "../cashback";
test('cashback at sum 500', () => {
    const result = calculateCashback(500);
    expect(result).toBe(0);
});

const dataList  = [
    ['gold', '100000', 5000],
    ['silver', '10000', 200],
    ['regular', 1000, 10],
    ['no', 500, 0]
];

const handler = test.each(dataList);
handler ('test cashback with %s and %i amount', 
    (status, amount, expected) => {
        const result = calculateCashback(amount);
        expect(result).toBe(expected);
    });