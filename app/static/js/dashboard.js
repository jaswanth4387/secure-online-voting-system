// ==========================================
// DASHBOARD JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("JanVote Dashboard Loaded");


    // ======================================
    // LIVE CLOCK
    // ======================================

    function updateDashboardClock() {

        const clock =
            document.getElementById(
                "dashboardClock"
            );

        if (clock) {

            const now = new Date();

            clock.innerHTML =
                now.toLocaleString();

        }

    }

    setInterval(
        updateDashboardClock,
        1000
    );

    updateDashboardClock();


    // ======================================
    // ANIMATE DASHBOARD NUMBERS
    // ======================================

    function animateCounter(
        element,
        start,
        end,
        duration
    ) {

        let startTime = null;

        function animation(currentTime) {

            if (!startTime)
                startTime = currentTime;

            const progress =
                Math.min(
                    (
                        currentTime - startTime
                    ) / duration,
                    1
                );

            element.innerHTML =
                Math.floor(
                    progress * (end - start)
                    + start
                );

            if (progress < 1) {

                requestAnimationFrame(
                    animation
                );

            }

        }

        requestAnimationFrame(
            animation
        );

    }


    // ======================================
    // START COUNTER ANIMATION
    // ======================================

    const counters =
        document.querySelectorAll(
            ".stats-number"
        );

    counters.forEach((counter) => {

        const target =
            parseInt(
                counter.dataset.value
            );

        animateCounter(
            counter,
            0,
            target,
            1500
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
            bar.getAttribute(
                "data-width"
            );

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width =
                width + "%";

        }, 300);

    });


    // ======================================
    // LIVE STATUS DOT
    // ======================================

    const liveDots =
        document.querySelectorAll(
            ".live-indicator"
        );

    liveDots.forEach((dot) => {

        setInterval(() => {

            dot.classList.toggle(
                "opacity-50"
            );

        }, 1000);

    });


    // ======================================
    // DASHBOARD CARD HOVER EFFECT
    // ======================================

    const cards =
        document.querySelectorAll(
            ".stats-card"
        );

    cards.forEach((card) => {

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
    // REFRESH DASHBOARD
    // ======================================

    const refreshButton =
        document.getElementById(
            "refreshDashboard"
        );

    if (refreshButton) {

        refreshButton.addEventListener(
            "click",
            function () {

                location.reload();

            }
        );

    }


    // ======================================
    // QUICK ACTION BUTTONS
    // ======================================

    const quickButtons =
        document.querySelectorAll(
            ".quick-action-btn"
        );

    quickButtons.forEach((button) => {

        button.addEventListener(
            "mouseenter",
            function () {

                button.style.transform =
                    "translateY(-3px)";

            }
        );

        button.addEventListener(
            "mouseleave",
            function () {

                button.style.transform =
                    "translateY(0px)";

            }
        );

    });


    // ======================================
    // TABLE SEARCH
    // ======================================

    const tableSearch =
        document.getElementById(
            "dashboardSearch"
        );

    if (tableSearch) {

        tableSearch.addEventListener(
            "keyup",
            function () {

                const value =
                    this.value.toLowerCase();

                const rows =
                    document.querySelectorAll(
                        ".dashboard-table tbody tr"
                    );

                rows.forEach((row) => {

                    const rowText =
                        row.innerText.toLowerCase();

                    row.style.display =
                        rowText.includes(value)
                            ? ""
                            : "none";

                });

            }
        );

    }


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
    // SHOW DASHBOARD NOTIFICATION
    // ======================================

    function showDashboardNotification(
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

        notification.style.borderRadius =
            "12px";

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
    // SYSTEM STATUS CHECK
    // ======================================

    function dashboardHealthCheck() {

        console.log(
            "Dashboard System Operational"
        );

    }

    setInterval(
        dashboardHealthCheck,
        30000
    );


    // ======================================
    // AUTO REFRESH DASHBOARD DATA
    // ======================================

    function autoRefreshDashboard() {

        console.log(
            "Refreshing dashboard statistics..."
        );

    }

    setInterval(
        autoRefreshDashboard,
        120000
    );


    // ======================================
    // EXPORT DASHBOARD TABLE
    // ======================================

    const exportButton =
        document.getElementById(
            "exportDashboard"
        );

    if (exportButton) {

        exportButton.addEventListener(
            "click",
            function () {

                const table =
                    document.querySelector(
                        ".dashboard-table table"
                    );

                if (!table) {

                    alert(
                        "No table available for export."
                    );

                    return;

                }

                let csv = [];

                const rows =
                    table.querySelectorAll("tr");

                rows.forEach((row) => {

                    const cols =
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
                    "dashboard_report.csv";

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
    // SECURITY ALERT DEMO
    // ======================================

    const securityAlertButton =
        document.getElementById(
            "securityAlertDemo"
        );

    if (securityAlertButton) {

        securityAlertButton.addEventListener(
            "click",
            function () {

                showDashboardNotification(
                    "Security alert monitoring activated.",
                    "warning"
                );

            }
        );

    }


    // ======================================
    // APPLICATION STATUS FILTER
    // ======================================

    const statusFilter =
        document.getElementById(
            "statusFilter"
        );

    if (statusFilter) {

        statusFilter.addEventListener(
            "change",
            function () {

                const value =
                    this.value.toLowerCase();

                const rows =
                    document.querySelectorAll(
                        ".dashboard-table tbody tr"
                    );

                rows.forEach((row) => {

                    if (
                        value === "all"
                    ) {

                        row.style.display = "";

                        return;

                    }

                    const rowText =
                        row.innerText.toLowerCase();

                    row.style.display =
                        rowText.includes(value)
                            ? ""
                            : "none";

                });

            }
        );

    }

});