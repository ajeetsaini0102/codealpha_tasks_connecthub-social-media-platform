const likeButtons = document.querySelectorAll(".like-button");

likeButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        button.classList.add("liked");

    });

});