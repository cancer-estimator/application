// add button related to extended questions
function addExtendedQuestions(extendedQuestions) {
    document.getElementById("extendProfile").addEventListener("click", function () {
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
  });
}
