// ================= GLOBAL INIT =================
document.addEventListener("DOMContentLoaded", () => {
    initNavbarHighlight();
    initVoteSystem();
    initFormValidation();
    initSmoothScroll();
    initOTP();
    loadResults();
});

// ================= NAVBAR ACTIVE LINK =================
function initNavbarHighlight() {
    const links = document.querySelectorAll(".nav-link");

    links.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add("active");
        }
    });
}


// ================= VOTING SYSTEM =================
function initVoteSystem() {
    const candidates = document.querySelectorAll(".candidate-card");
    let selectedCandidate = null;

    const alreadyVoted = getVote();

    if (alreadyVoted) {
        showToast(`⚠ You already voted for ${alreadyVoted}`);
    }

    candidates.forEach(card => {
        card.addEventListener("click", () => {

            if (alreadyVoted) {
                showToast("❌ Voting already done!");
                return;
            }

            candidates.forEach(c => c.classList.remove("selected"));
            card.classList.add("selected");

            selectedCandidate = card.querySelector("h5")?.innerText;
            showVoteConfirmation(selectedCandidate);
        });
    });

    const submitBtn = document.querySelector(".submit-btn");

    if (submitBtn) {
        submitBtn.addEventListener("click", (e) => {
            if (!selectedCandidate) {
                e.preventDefault();
                showToast("⚠ Select a candidate first!");
            } else {
                saveVote(selectedCandidate);
                updateResults(selectedCandidate);
                showToast(`✅ Vote saved for ${selectedCandidate}`);

                setTimeout(() => {
                    window.location.href = "confirmation.html";
                }, 1200);
            }
        });
    }
}

// ================= SHOW VOTE CONFIRM =================
function showVoteConfirmation(name) {
    let box = document.querySelector(".vote-confirm");

    if (!box) {
        box = document.createElement("div");
        box.className = "vote-confirm";
        document.querySelector(".vote-container")?.appendChild(box);
    }

    box.innerHTML = `
        <h5>Selected Candidate:</h5>
        <p><strong>${name}</strong></p>
    `;
}


// ================= FORM VALIDATION =================
function initFormValidation() {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", (e) => {

            const inputs = form.querySelectorAll("input[required], textarea[required], select[required]");
            let valid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    valid = false;
                    input.style.border = "2px solid red";
                } else {
                    input.style.border = "";
                }
            });

            if (!valid) {
                e.preventDefault();
                alert("⚠ Please fill all required fields!");
            }
        });
    });
}


// ================= SMOOTH SCROLL =================
function initSmoothScroll() {
    document.querySelectorAll("a[href^='#']").forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {
                target.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });
}


// ================= EXTRA: ANIMATION ON SCROLL =================
window.addEventListener("scroll", () => {
    const elements = document.querySelectorAll(".action-card, .form-card, .candidate-card");

    elements.forEach(el => {
        const position = el.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            el.style.opacity = "1";
            el.style.transform = "translateY(0)";
        }
    });
});

// ================= OTP SIMULATION =================
function generateOTP() {
    return Math.floor(100000 + Math.random() * 900000);
}

let currentOTP = null;

function initOTP() {
    const verifyBtns = document.querySelectorAll("button");

    verifyBtns.forEach(btn => {
        if (btn.innerText.includes("Verify")) {
            btn.addEventListener("click", () => {
                currentOTP = generateOTP();
                showToast(`OTP Sent: ${currentOTP} (demo)`);

                const userInput = prompt("Enter OTP:");

                if (userInput == currentOTP) {
                    showToast("✅ OTP Verified");
                } else {
                    showToast("❌ Invalid OTP");
                }
            });
        }
    });
}

// ================= STORE VOTE =================
function saveVote(candidate) {
    localStorage.setItem("votedCandidate", candidate);
}

function getVote() {
    return localStorage.getItem("votedCandidate");
}
// ================= RESULTS SYSTEM =================
function updateResults(candidate) {
    let results = JSON.parse(localStorage.getItem("results")) || {};

    if (!results[candidate]) {
        results[candidate] = 0;
    }

    results[candidate]++;

    localStorage.setItem("results", JSON.stringify(results));
}

function loadResults() {
    const table = document.querySelector("tbody");

    if (!table) return;

    const results = JSON.parse(localStorage.getItem("results")) || {};

    table.innerHTML = "";

    for (let candidate in results) {
        const votes = results[candidate];

        const row = `
            <tr>
                <td>${candidate}</td>
                <td>${votes}</td>
                <td>
                    <div class="progress">
                        <div class="progress-bar bg-success" style="width:${votes * 10}%">
                            ${votes}
                        </div>
                    </div>
                </td>
            </tr>
        `;

        table.innerHTML += row;
    }
}

// ================= TOAST SYSTEM =================
function showToast(message) {
    let toast = document.createElement("div");
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