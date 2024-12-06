export const calcSummaryRate = function (dailyRation) {

    let myObjects = ["breakfast","lunch", "coffee-break","afternoon-tea","dinner"];
    let sum = 0;
    for (const element of myObjects) {
        if(dailyRation.hasOwnProperty(element)) {
        sum += dailyRation[element];
        }
    }
    dailyRation.summary = sum;
    return dailyRation;
}

let mondayRation = {
    breakfast: 1240,
    lunch: 765,
    dinner: 564,
};

mondayRation = calcSummaryRate(mondayRation);
console.log(mondayRation);
console.log(mondayRation.summary)

const tuesdayRation = {
    breakfast: 780,
    "coffee-break": 115,
    lunch: 975,
    "afternoon-tea": 230,
    dinner: 441,
    summary: 0,
};
calcSummaryRate(tuesdayRation);
console.log(tuesdayRation.summary);