// add button related to extended questions
function buttonExtendProfile(fields) {
    var extendedQuestionsDiv = document.getElementById("extendedQuestions");
    if (extendedQuestionsDiv.innerHTML === "") {
        extendedQuestionsDiv.innerHTML += extendedQuestions;
    }
    var blocked = extendedQuestionsDiv.style.display === "none"
    extendedQuestionsDiv.style.display = blocked ? "block" : "none";
    if (extendedQuestionsDiv.style.display === "block") {
        document.getElementById("extendProfile").innerText = "Collapse"
    } else {
        document.getElementById("extendProfile").innerText = "Add extra symptons for lung cancer risk estimation"
    }
}


function addExtendedQuestions(extendedQuestions, fields, initialize=false) {
    let extendedQuestionsDiv = document.getElementById("extendedQuestions");
    // initialize button shown if it's true
    if (initialize === true) {
        buttonExtendProfile(fields)
    }
    document.getElementById("extendProfile").addEventListener("click", () => buttonExtendProfile(fields));
}
