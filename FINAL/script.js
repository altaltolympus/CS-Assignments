const brief = document.getElementById("meeting-the-brief");
const investigation = document.getElementById("investigation");
const planning = document.getElementById("planning-and-design");
const creation = document.getElementById("creation");
const evaluation = document.getElementById("evaluation");

let briefWords = document.getElementById("brief-words");
let investigationWords = document.getElementById("investigation-words");
let planningWords = document.getElementById("planning-words");
let creationWords = document.getElementById("creation-words");
let evaluationWords = document.getElementById("evaluation-words");
let totalWords = document.getElementById("total-words");

let sections = [brief, investigation, planning, creation, evaluation];
let tableCells = [briefWords, investigationWords, planningWords, creationWords, evaluationWords];

function countWords(section) {
    const words = section.querySelectorAll("p, h3, h4");
    let count = 0;
    for (const el of words) {
        count += el.innerText.split(" ").length;
    }
    return count;
}

function sum(words) {
    let total = 0;
    for (let count of words) {
        total += parseInt(count.innerHTML);
    }

    return total;
}

sections.forEach((item, index) => {
    tableCells[index].innerText = countWords(item);
});

totalWords.innerText = sum(tableCells);
