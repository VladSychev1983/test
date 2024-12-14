
export const sortContacts = function (contacts) {
    return contacts.sort((a,b) => a.name.localeCompare(b.name));
}
let items = [{ name: "Ян" }, { name: "Борис" }, { name: "Александр" }];
let result = sortContacts(items);
console.log(result)
