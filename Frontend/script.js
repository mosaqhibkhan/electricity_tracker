const backendUrl = "http://127.0.0.1:5000";

function trackUsage() {
    const monthlyLimit = document.getElementById("monthly-limit").value;
    const currentUsage = document.getElementById("current-usage").value;

    fetch(`${backendUrl}/track_usage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ monthly_limit: monthlyLimit, current_usage: currentUsage }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("remaining-budget").innerText =
            `Remaining Budget: ${data.remaining_budget} kWh`;
    })
    .catch(error => console.error("Error:", error));
}

function toggleAppliance(action) {
    const appliance = document.getElementById("appliance").value;

    fetch(`${backendUrl}/toggle_appliance`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ appliance, action }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("appliance-status").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}
