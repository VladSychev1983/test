let x = 3;
function test() {
    x = 4;
    console.log(x);
}
test();
console.log(global);

console.log(__dirname);
console.log(__filename);
console.log(exports)
console.log(module)
//print all process variable
console.log(process)
//to get os name
console.log(process.env["OS"])