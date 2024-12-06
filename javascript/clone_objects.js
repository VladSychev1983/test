//MDN example deep copy objects.
//const ingredientsList = ["noodles", { list: ["eggs", "flour", "water"] }];
//const ingredientsListDeepCopy = JSON.parse(JSON.stringify(ingredientsList));

export const cloneObj = function (obj) {
    const ObjDeepCopy = JSON.parse(JSON.stringify(obj))
    return ObjDeepCopy;
};

//// Spread Method копирует также функции вложенные в объект.
export const clone = function (obj) {
let ObjDeepCopy = { ...obj };
return ObjDeepCopy;
}