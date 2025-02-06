export class Client {};
export const timeout = 5;
const defaultClient = new Client();
export default defaultClient;

//no export variable example.
let data = [1, 2, 3, 4, 5];
console.log('logs.js executed!');