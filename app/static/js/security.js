// ==========================================
// SECURITY DASHBOARD JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Security Dashboard Loaded");


    // ======================================
    // LIVE SECURITY CLOCK
    // ======================================

    function updateSecurityClock() {

        const clock =
            document.getElementById(
                "securityClock"
            );

        if (clock) {

            const now = new Date();

            clock.innerHTML =
                now.toLocaleString();

        }

    }

    setInterval(
        updateSecurityClock,
        1000
    );

    updateSecurityClock();


    // ======================================
    // LIVE SECURITY STATUS
    // ======================================

    const liveDots =
        document.querySelectorAll(
            ".live-dot"
        );

    liveDots.forEach((dot) => {

        setInterval(() => {

            dot.classList.toggle(
                "opacity-50"
            );

        }, 1000);

    });


    // ======================================
    // ANIMATE SECURITY COUNTERS
    // ======================================

    function animateSecurityCounter(
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

    const securityCounters =
        document.querySelectorAll(
            ".security-counter"
        );

    securityCounters.forEach((counter) => {

        const target =
            parseInt(
                counter.dataset.value
            );

        animateSecurityCounter(
            counter,
            0,
            target,
            1500
        );

    });


    // ======================================
    // FILTER SECURITY TABLE
    // ======================================

    const securitySearch =
        document.getElementById(
            "securitySearch"
        );

    if (securitySearch) {

        securitySearch.addEventListener(
            "keyup",
            function () {

                const value =
                    this.value.toLowerCase();

                const rows =
                    document.querySelectorAll(
                        ".security-table tbody tr"
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
    // RISK FILTER
    // ======================================

    const riskFilter =
        document.getElementById(
            "riskFilter"
        );

    if (riskFilter) {

        riskFilter.addEventListener(
            "change",
            function () {

                const value =
                    this.value.toLowerCase();

                const rows =
                    document.querySelectorAll(
                        ".security-table tbody tr"
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


    // ======================================
    // REFRESH SECURITY DASHBOARD
    // ======================================

    const refreshButton =
        document.getElementById(
            "refreshSecurityDashboard"
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
    // SECURITY ALERT NOTIFICATION
    // ======================================

    function showSecurityNotification(
        message,
        type = "danger"
    ) {

        const notification =
            document.createElement("div");

        notification.className =
            `alert alert-${type} position-fixed`;

        notification.style.top = "20px";

        notification.style.right = "20px";

        notification.style.zIndex = "9999";

        notification.style.minWidth = "320px";

        notification.style.borderRadius =
            "12px";

        notification.innerHTML = `
            <strong>Security Alert:</strong>
            ${message}
        `;

        document.body.appendChild(
            notification
        );

        setTimeout(() => {

            notification.remove();

        }, 5000);

    }


    // ======================================
    // SECURITY BUTTON ACTIONS
    // ======================================

    const investigateButtons =
        document.querySelectorAll(
            ".investigate-btn"
        );

    investigateButtons.forEach((button) => {

        button.addEventListener(
            "click",
            function () {

                showSecurityNotification(
                    "Investigation process started.",
                    "warning"
                );

            }
        );

    });


    // ======================================
    // BLOCK IP BUTTON
    // ======================================

    const blockButtons =
        document.querySelectorAll(
            ".block-ip-btn"
        );

    blockButtons.forEach((button) => {

        button.addEventListener(
            "click",
            function () {

                const confirmBlock =
                    confirm(
                        "Are you sure you want to block this IP?"
                    );

                if (confirmBlock) {

                    showSecurityNotification(
                        "IP address blocked successfully.",
                        "danger"
                    );

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
    // AUTO REFRESH SECURITY DATA
    // ======================================

    function autoRefreshSecurity() {

        console.log(
            "Refreshing security monitoring data..."
        );

    }

    setInterval(
        autoRefreshSecurity,
        60000
    );


    // ======================================
    // EXPORT SECURITY REPORT
    // ======================================

    const exportButton =
        document.getElementById(
            "exportSecurityReport"
        );

    if (exportButton) {

        exportButton.addEventListener(
            "click",
            function () {

                const table =
                    document.querySelector(
                        ".security-table"
                    );

                if (!table) {

                    alert(
                        "No security table found."
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
                    "security_report.csv";

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
    // SYSTEM THREAT SIMULATION
    // ======================================

    function simulateThreatMonitoring() {

        console.log(
            "Threat monitoring active..."
        );

    }

    setInterval(
        simulateThreatMonitoring,
        30000
    );


    // ======================================
    // SECURITY HEALTH CHECK
    // ======================================

    function securityHealthCheck() {

        console.log(
            "Security systems operational."
        );

    }

    setInterval(
        securityHealthCheck,
        120000
    );

});