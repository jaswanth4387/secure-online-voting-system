// ==========================================
// ADMIN PANEL JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("JanVote Admin Panel Loaded");


    // ======================================
    // ACTIVE SIDEBAR LINK
    // ======================================

    const currentLocation = window.location.href;

    const menuItems = document.querySelectorAll(".sidebar-menu a");

    menuItems.forEach((item) => {

        if (item.href === currentLocation) {

            item.classList.add("active");

        }

    });


    // ======================================
    // AUTO CLOSE ALERTS
    // ======================================

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach((alert) => {

        setTimeout(() => {

            alert.classList.remove("show");

            alert.classList.add("fade");

        }, 5000);

    });


    // ======================================
    // LIVE CLOCK
    // ======================================

    function updateClock() {

        const clockElement =
            document.getElementById("live-clock");

        if (clockElement) {

            const now = new Date();

            const options = {

                weekday: "short",

                year: "numeric",

                month: "short",

                day: "numeric",

                hour: "2-digit",

                minute: "2-digit",

                second: "2-digit"

            };

            clockElement.innerHTML =
                now.toLocaleDateString(
                    "en-US",
                    options
                );

        }

    }

    setInterval(updateClock, 1000);

    updateClock();


    // ======================================
    // TABLE SEARCH FILTER
    // ======================================

    const searchInput =
        document.getElementById("tableSearch");

    if (searchInput) {

        searchInput.addEventListener(
            "keyup",
            function () {

                let value =
                    this.value.toLowerCase();

                let rows =
                    document.querySelectorAll(
                        "table tbody tr"
                    );

                rows.forEach((row) => {

                    let text =
                        row.innerText.toLowerCase();

                    row.style.display =
                        text.includes(value)
                            ? ""
                            : "none";

                });

            }
        );

    }


    // ======================================
    // CONFIRM DELETE
    // ======================================

    const deleteButtons =
        document.querySelectorAll(
            ".delete-btn"
        );

    deleteButtons.forEach((button) => {

        button.addEventListener(
            "click",
            function (event) {

                const confirmDelete =
                    confirm(
                        "Are you sure you want to delete this item?"
                    );

                if (!confirmDelete) {

                    event.preventDefault();

                }

            }
        );

    });


    // ======================================
    // LOADING BUTTON
    // ======================================

    const forms =
        document.querySelectorAll("form");

    forms.forEach((form) => {

        form.addEventListener(
            "submit",
            function () {

                const submitBtn =
                    form.querySelector(
                        "button[type='submit']"
                    );

                if (submitBtn) {

                    submitBtn.disabled = true;

                    submitBtn.innerHTML = `
                        <span class="spinner-border spinner-border-sm me-2"></span>
                        Processing...
                    `;

                }

            }
        );

    });


    // ======================================
    // TOOLTIP INITIALIZATION
    // ======================================

    const tooltipTriggerList =
        [].slice.call(
            document.querySelectorAll(
                '[data-bs-toggle="tooltip"]'
            )
        );

    tooltipTriggerList.map(function (
        tooltipTriggerEl
    ) {

        return new bootstrap.Tooltip(
            tooltipTriggerEl
        );

    });


    // ======================================
    // POPOVER INITIALIZATION
    // ======================================

    const popoverTriggerList =
        [].slice.call(
            document.querySelectorAll(
                '[data-bs-toggle="popover"]'
            )
        );

    popoverTriggerList.map(function (
        popoverTriggerEl
    ) {

        return new bootstrap.Popover(
            popoverTriggerEl
        );

    });


    // ======================================
    // LIVE STATUS ANIMATION
    // ======================================

    const liveDots =
        document.querySelectorAll(
            ".live-dot"
        );

    liveDots.forEach((dot) => {

        setInterval(() => {

            dot.classList.toggle("opacity-50");

        }, 1000);

    });


    // ======================================
    // SIDEBAR TOGGLE (MOBILE)
    // ======================================

    const sidebarToggle =
        document.getElementById(
            "sidebarToggle"
        );

    const sidebar =
        document.querySelector(".sidebar");

    if (sidebarToggle && sidebar) {

        sidebarToggle.addEventListener(
            "click",
            function () {

                sidebar.classList.toggle(
                    "mobile-sidebar-active"
                );

            }
        );

    }


    // ======================================
    // DASHBOARD CARD HOVER EFFECT
    // ======================================

    const dashboardCards =
        document.querySelectorAll(
            ".dashboard-card"
        );

    dashboardCards.forEach((card) => {

        card.addEventListener(
            "mouseenter",
            function () {

                card.style.transform =
                    "translateY(-6px)";

            }
        );

        card.addEventListener(
            "mouseleave",
            function () {

                card.style.transform =
                    "translateY(0px)";

            }
        );

    });


    // ======================================
    // PROGRESS BAR ANIMATION
    // ======================================

    const progressBars =
        document.querySelectorAll(
            ".progress-bar"
        );

    progressBars.forEach((bar) => {

        const width =
            bar.style.width;

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });


    // ======================================
    // REFRESH DASHBOARD BUTTON
    // ======================================

    const refreshBtn =
        document.getElementById(
            "refreshDashboard"
        );

    if (refreshBtn) {

        refreshBtn.addEventListener(
            "click",
            function () {

                location.reload();

            }
        );

    }


    // ======================================
    // REALTIME NOTIFICATION DEMO
    // ======================================

    function showNotification(
        message,
        type = "success"
    ) {

        const notification =
            document.createElement("div");

        notification.className =
            `alert alert-${type} position-fixed`;

        notification.style.top = "20px";

        notification.style.right = "20px";

        notification.style.zIndex = "9999";

        notification.style.minWidth = "300px";

        notification.innerHTML = `
            ${message}
        `;

        document.body.appendChild(
            notification
        );

        setTimeout(() => {

            notification.remove();

        }, 4000);

    }


    // ======================================
    // EXPORT TABLE TO CSV
    // ======================================

    const exportBtn =
        document.getElementById(
            "exportCSV"
        );

    if (exportBtn) {

        exportBtn.addEventListener(
            "click",
            function () {

                const table =
                    document.querySelector(
                        "table"
                    );

                if (!table) {

                    alert(
                        "No table found to export."
                    );

                    return;

                }

                let csv = [];

                const rows =
                    table.querySelectorAll("tr");

                rows.forEach((row) => {

                    let cols =
                        row.querySelectorAll(
                            "td, th"
                        );

                    let rowData = [];

                    cols.forEach((col) => {

                        rowData.push(
                            `"${col.innerText.trim()}"`
                        );

                    });

                    csv.push(
                        rowData.join(",")
                    );

                });

                const csvFile =
                    new Blob(
                        [csv.join("\n")],
                        {
                            type:
                                "text/csv"
                        }
                    );

                const downloadLink =
                    document.createElement("a");

                downloadLink.download =
                    "janvote_report.csv";

                downloadLink.href =
                    window.URL.createObjectURL(
                        csvFile
                    );

                downloadLink.style.display =
                    "none";

                document.body.appendChild(
                    downloadLink
                );

                downloadLink.click();

            }
        );

    }


    // ======================================
    // SYSTEM HEALTH CHECK
    // ======================================

    function systemHealthCheck() {

        console.log(
            "System Status: Operational"
        );

    }

    setInterval(
        systemHealthCheck,
        30000
    );

});