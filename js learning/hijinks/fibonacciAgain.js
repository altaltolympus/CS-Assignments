// #region variable block
let last = 1;
let current = 0;
let next = 0;
let iterations = 0;
let output = document.getElementById("fibOutput");
let fibCounter = document.getElementById("fibIterations");
let iterationInput = document.getElementById("fibLoop");
let iterationLimit = document.getElementById("fibLoop").value;
let loop;
let active = false;
let startButton = document.getElementById("fibStart");

// #region start button updater
iterationInput.addEventListener("change", () => {
    iterationLimit = iterationInput.value;
    console.debug(`Iteration limit changed to ${iterationLimit}`);
    if (iterations >= iterationLimit) blockStart();
    else enableStart();
})

// #region berateUser()
function berateUser() {
    console.debug(`iterationLimit input: ${iterationLimit}`);
    if (iterationLimit == "" || iterationLimit == 0) {
        iterationLimit = 32678;
    }
    if (isNaN(parseInt(iterationLimit))) {
            window.alert("fibonacci is turning in his grave right now");
            console.warn(`things were going fine until YOU decided to ruin them by inputting "${iterationLimit}" or some shit`);
            return true;
        }
    else {
        return false;
    }
}

// #region fibonacci()
function fibonacci() {
    iterations++;
    console.log(`Iteration: ${iterations} | Output: ${current}`);
    output.innerText = current;
    fibCounter.innerText = `Iterations: ${iterations}`;
    next = current + last;
    last = current;
    current = next;
}

// #region fibReset()
function fibReset() {
    clearInterval(loop);
    last = 1;
    current = 0;
    next = 0;
    iterations = 0;
    output.innerText = "";
    fibCounter.innerText = `Iterations: ${iterations}`;
    active = false;
}

// #region fibLoop()
function fibLoop() {
    loop = setInterval(() => {
        fibonacci();
        if (iterations >= iterationLimit) clearInterval(loop);
    }, 500);
    active = false;
}

// #region fibonacciStart()
function fibonacciStart() {
    if (berateUser(iterationLimit)) return;
    if (active) {
        window.alert("Please wait for the current loop to finish!");
        console.log("Start attempted while loop active")
        return;
    }
    if (iterations >= iterationLimit) {
        window.alert("Iteration limit has been reached, either increase limit in the text box or reset");
        return;
    }
    else {
        active = true;
        blockStart();
        fibLoop();
    }
}

// #region blockStart()
function blockStart() {
    startButton.style.backgroundColor = "#32323a";
    startButton.style.color = "#32323a";
    startButton.onclick = "";
}

// #region enableStart()
function enableStart() {
    startButton.style.backgroundColor = "#eee";
    startButton.style.color = "#111";
    startButton.onclick = fibonacciStart();
}
