let yesButton = document.getElementById("yes");
let noButton = document.getElementById("no");
function yesClick() {
    let age = parseInt(document.getElementById("age").value);
    if (isNaN(age)) {
        window.alert("you are a disgrace.");
        return;
    }
    if (age > 16) {
        window.alert("good job you may have a license now");
    } else {
        window.alert("you are a little baby there is no way you have a provisional driving license");
    }
}
function noClick() {
    window.alert("get a provisional license; you are silly");
}
