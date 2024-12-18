
export const sortContacts = function (contacts) {
    return contacts.sort((a,b) => a.name.localeCompare(b.name));
}
let items = [{ name: "Ян" }, { name: "Борис" }, { name: "Александр" }];
let result = sortContacts(items);
console.log(result)


const arr = [ 10, 20, 25, 100, 40]
// Pass the comparator to to sort in reverse order
arr.sort((a, b) => b - a)        //в порядке убывания.   arr.sort((a,b) => b - a) 
                                //в порядке возрастания. arr.sort((a,b) => a - b)

console.log(arr)


let employees = {
    john: { age: 28, salary: 3000 },
    jane: { age: 32, salary: 4000 },
    doe: { age: 22, salary: 2500 }
};

let sortedBySalary = Object.fromEntries(
    Object.entries(employees).sort(([, a], [, b]) => a.salary - b.salary)
);

console.log(sortedBySalary);
// Output: { doe: { age: 22, salary: 2500 }, john: { age: 28, salary: 3000 }, jane: { age: 32, salary: 4000 } }