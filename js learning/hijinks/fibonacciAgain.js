let last = 1,
    current = 0;
    next = 0;
    iterations = 0;
    output = document.getElementById("fibOutput");
    fibCounter = document.getElementById("fibIterations");

function fibonacci() {
    iterations++;
    console.log(`Iteration: ${iterations} | Output: ${current}`);
    output.innerText = current;
    fibCounter.innerText = `Iterations: ${iterations}`
    next = current + last;
    last = current;
    current = next;
}

function fibReset() {
    last = 1;
    current = 0;
    next = 0;
    iterations = 0;
    output.innerText = ""
}