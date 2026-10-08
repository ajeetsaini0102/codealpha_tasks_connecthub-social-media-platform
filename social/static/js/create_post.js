const postTextarea = document.querySelector(".post-textarea");

const characterCount = document.createElement("p");

characterCount.className = "character-count";

characterCount.textContent = "0 characters";

postTextarea.parentNode.insertBefore(characterCount, postTextarea.nextSibling);


postTextarea.addEventListener("input", function () {

    const length = postTextarea.value.length;

    characterCount.textContent = length + " characters";

});