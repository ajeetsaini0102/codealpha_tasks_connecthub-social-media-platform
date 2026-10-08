const profilePosts = document.querySelectorAll(".profile-post");

profilePosts.forEach(function (post) {

    post.addEventListener("click", function () {

        post.classList.toggle("active");

    });

});