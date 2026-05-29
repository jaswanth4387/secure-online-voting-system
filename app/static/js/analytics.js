// ==========================================
// ANALYTICS DASHBOARD JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Analytics Dashboard Loaded");


    // ======================================
    // LIVE CLOCK
    // ======================================

    function updateAnalyticsClock() {

        const clock =
            document.getElementById(
                "analyticsClock"
            );

        if (clock) {

            const now = new Date();

            clock.innerHTML =
                now.toLocaleString();

        }

    }

    setInterval(
        updateAnalyticsClock,
        1000
    );

    updateAnalyticsClock();


    // ======================================
    // ANIMATE NUMBERS
    // ======================================

    function animateValue(
        element,
        start,
        end,
        duration
    ) {

        let startTimestamp = null;

        const step = (timestamp) => {

            if (!startTimestamp)
                startTimestamp = timestamp;

            const progress = Math.min(
                (timestamp - startTimestamp)
                / duration,
                1
            );

            element.innerHTML =
                Math.floor(
                    progress * (end - start)
                    + start
                );

            if (progress < 1) {

                window.requestAnimationFrame(
                    step
                );

            }

        };

        window.requestAnimationFrame(
            step
        );

    }


    // ======================================
    // START NUMBER ANIMATION
    // ======================================

    const analyticsNumbers =
        document.querySelectorAll(
            ".analytics-number"
        );

    analyticsNumbers.forEach((number) => {

        const finalValue =
            parseInt(
                number.dataset.value
            );

        animateValue(
            number,
            0,
            finalValue,
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
    // FILTER ANALYTICS TABLE
    // ======================================

    const analyticsSearch =
        document.getElementById(
            "analyticsSearch"
        );

    if (analyticsSearch) {

        analyticsSearch.addEventListener(
            "keyup",
            function () {

                const value =
                    this.value.toLowerCase();

                const rows =
                    document.querySelectorAll(
                        ".analytics-table tbody tr"
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
    // REFRESH ANALYTICS
    // ======================================

    const refreshAnalytics =
        document.getElementById(
            "refreshAnalytics"
        );

    if (refreshAnalytics) {

        refreshAnalytics.addEventListener(
            "click",
            function () {

                location.reload();

            }
        );

    }


    // ======================================
    // EXPORT ANALYTICS
    // ======================================

    const exportAnalytics =
        document.getElementById(
            "exportAnalytics"
        );

    if (exportAnalytics) {

        exportAnalytics.addEventListener(
            "click",
            function () {

                const table =
                    document.querySelector(
                        ".analytics-table table"
                    );

                if (!table) {

                    alert(
                        "No analytics table found."
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
                    "analytics_report.csv";

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
    // LIVE STATUS PULSE
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
    // ANALYTICS CARD HOVER EFFECT
    // ======================================

    const analyticsCards =
        document.querySelectorAll(
            ".analytics-card"
        );

    analyticsCards.forEach((card) => {

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
    // MOCK LIVE ANALYTICS UPDATE
    // ======================================

    function updateLiveAnalytics() {

        console.log(
            "Analytics Updated"
        );

    }

    setInterval(
        updateLiveAnalytics,
        30000
    );


    // ======================================
    // CHART PLACEHOLDER INTERACTION
    // ======================================

    const chartAreas =
        document.querySelectorAll(
            ".chart-placeholder"
        );

    chartAreas.forEach((chart) => {

        chart.addEventListener(
            "click",
            function () {

                alert(
                    "Chart integration can be connected with Chart.js or ApexCharts."
                );

            }
        );

    });


    // ======================================
    // SHOW SUCCESS NOTIFICATION
    // ======================================

    function showAnalyticsNotification(
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
    // SYSTEM HEALTH MONITOR
    // ======================================

    function analyticsHealthMonitor() {

        console.log(
            "Analytics System Healthy"
        );

    }

    setInterval(
        analyticsHealthMonitor,
        60000
    );

});