let lastNum = 0,
    currentNum = 0,
    nextNum = 0;
let loop;
console.log(loop);
let output = document.getElementById("fibOutput");
function fibonacci(lastNum, currentNum, nextNum) {
    // for (let i = 0; i < 10; i++) {
    loop = setInterval(() => {
        if (currentNum == 0) {
            currentNum = 1;
            console.log(0);
            console.log(currentNum);
            output.innerText = currentNum;
        } else console.log(nextNum);
        output.innerText = nextNum;
        nextNum = currentNum + lastNum;
        lastNum = currentNum;
        currentNum = nextNum;
    }, 1000);
    // }
}

function stop(loop) {
    clearInterval(loop);
}
