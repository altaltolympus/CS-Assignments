let last = 1,
    current = 0;
    next = 0;
// let loop;
// console.log(loop);
let output = document.getElementById("fibOutput");
// function fibonacci(lastNum, currentNum, nextNum) {
//     // for (let i = 0; i < 10; i++) {
//     loop = setInterval(() => {
//         if (currentNum == 0) {
//             currentNum = 1;
//             console.log(0);
//             console.log(currentNum);
//             output.innerText = currentNum;
//         } else console.log(nextNum);
//         output.innerText = nextNum;
//         nextNum = currentNum + lastNum;
//         lastNum = currentNum;
//         currentNum = nextNum;
//     }, 1000);
//     // }
// }

// function fibonacci(last, current, next, iterations) {
//     for (i = 0; i < 20; i++) {
//     if (current == 0) current = 1;
//     console.log(last);
//     current += last;
//     last = current
// }}

function fibonacci() {
    console.log(current);
    output.innerText = current
    next = current + last;
    last = current;
    current = next;
}

function fibReset() {
    last = 1;
    current = 0;
    next = 0;
    output.innerText = ""
}