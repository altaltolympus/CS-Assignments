let dieSelect = document.getElementById("dieSelector");
dieSelect.value = "6"; // how do you do default values on a <select>? never mind this is good enough
let diceAmount = document.getElementById("diceAmount");
diceAmount.value = 1;
let dieResults = [];
let diceOutput = document.getElementById("diceOutput");
let dieSize = 6;
let dieNumber = 1;
let diceFinalOutput = "";

dieSelect.addEventListener("change", () => {
    dieSize = parseInt(dieSelect.value);
    console.log(`Current dice: ${dieNumber}d${dieSize}`);
});
diceAmount.addEventListener("change", () => {
    dieNumber = parseInt(diceAmount.value);
    console.log(`Current dice: ${dieNumber}d${dieSize}`);
})

function constructDiceOutput() {
    for (let number of dieResults) diceFinalOutput += `+ ${number} `;
    diceFinalOutput = diceFinalOutput.slice(2);
    diceFinalOutput += `= `
}

function roll() {
    reset();
    for (let rolls = 0; rolls < dieNumber; rolls++) {
        dieResults.push(Math.floor((Math.random() * dieSize) + 1))
        console.log(`rolled ${dieNumber}d${dieSize} and got ${Math.floor((Math.random() * dieSize) + 1)}`)
        console.log(dieResults)
    }
    diceOutput.innerText = dieResults
}

function reset() {
    dieResults = [];
    diceOutput.innerText = "";
}