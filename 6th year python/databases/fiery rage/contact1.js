const firebaseConfig = {
    apiKey: "AIzaSyAvu6RbHhgV5lDRFztyz7A2NYSLNm243kU",
    authDomain: "forcedolympus.firebaseapp.com",
    databaseURL: "https://forcedolympus-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "forcedolympus",
    storageBucket: "forcedolympus.firebasestorage.app",
    messagingSenderId: "1036044356983",
    appId: "1:1036044356983:web:4d90ce42ab8b5cab722572",
};

// const btn = document.getElementById("submit-data");
// btn.addEventListener("click", saveContacts);

// // Submit clicked so post the data to the server
// function saveContacts() {
//     alert("SUBMIT clicked!!!");
//     const emailField = document.getElementById("email");
//     const emailFieldValue = emailField.value;
//     alert(emailFieldValue);
//     // Task 2E - read the data from the email field
// } // <-- GOTCHA!
firebase.initializeApp(firebaseConfig);
const connection = firebase.database().ref("/contacts");
function onSubmit(e) {
    e.preventDefault();
    let emailContent = document.getElementById("email").value;
    const data = connection.push();
    data.set({ email: emailContent });
    emailContent = "";
}
document.getElementById("theform").addEventListener("submit", onSubmit);
