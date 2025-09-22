function rectangle() {
    let length = parseInt(document.getElementById("length").value);
    let width = parseInt(document.getElementById("width").value);
    let output = document.getElementById("rectOutput");
    let area = calculateArea(length, width);
    if (isNaN(area)) {
        output.innerText = "Thy rectangle be not a true shape; it be a work of sorcery";
    } else if (length == width) {
        output.innerText = `Thy rectangle be naught but a square which bears delusions of its own grandeur, and hath a breadth of ${area}.`;
    } else {
        output.innerText = `Thy rectangle hath a breadth of ${area}.`;
    }
}
function calculateArea(length, width) {
    let area = length * width;
    return area;
}
