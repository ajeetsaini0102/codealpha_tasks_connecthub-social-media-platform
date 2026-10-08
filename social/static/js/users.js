const followButtons = document.querySelectorAll(".follow-button");
const unfollowButtons = document.querySelectorAll(".unfollow-button");

followButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        button.textContent = "Following...";

    });

});

unfollowButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        button.textContent = "Unfollowing...";

    });

});