let last = 1;
let current = 0;
let next = 0;
let iterations = 0;
let output = document.getElementById("fibOutput");
let fibCounter = document.getElementById("fibIterations");
let iterationLimit = document.getElementById("fibLoop").value;
let loop;

function berateUser(num) {
    if (isNaN(parseInt(num))) {
        window.alert("fibonacci is turning in his grave right now");
        console.warn(`things were going fine until YOU decided to ruin them by inputting "${num}" or some shit`);
        return true;
    } else {
        return false;
    }
}

function fibonacci() {
    iterations++;
    console.log(`Iteration: ${iterations} | Output: ${current}`);
    output.innerText = current;
    fibCounter.innerText = `Iterations: ${iterations}`;
    next = current + last;
    last = current;
    current = next;
}

function fibReset() {
    last = 1;
    current = 0;
    next = 0;
    iterations = 0;
    output.innerText = "";
    fibCounter.innerText = `Iterations: ${iterations}`;
}

function fibLoop() {
    // for (let i = 0; i <= iterationLimit; i++) {
    loop = setInterval(() => {
        fibonacci();
        iterations++;
        if (iterations > iterationLimit) clearInterval(loop);
    }, 500);
}

function fibonacciStart() {
    if (berateUser(iterationLimit)) return;
    fibLoop();
}
