// Smooth animation on button click

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const button = document.querySelector("button");

        button.innerHTML =
            "🤖 AI is analyzing your profile...";

        button.disabled = true;

    });

}

// Fade in animation

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});