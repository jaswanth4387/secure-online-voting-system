document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("voterApplicationForm");

    if(form){

        form.addEventListener("submit", (e) => {

            e.preventDefault();

            showToast("Application Submitted Successfully!");

            setTimeout(() => {

                window.location.href = "/";

            }, 1500);

        });

    }

});

function showToast(message){

    const toast = document.createElement("div");

    toast.className = "custom-toast";

    toast.innerText = message;

    document.body.appendChild(toast);

    setTimeout(() => {

        toast.classList.add("show");

    }, 100);

    setTimeout(() => {

        toast.remove();

    }, 3000);

}