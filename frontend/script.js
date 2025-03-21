const API_BASE_URL = "http://127.0.0.1:5000";

// Fetch and display energy usage
async function trackUsage() {
    try {
        const response = await fetch(`${API_BASE_URL}/get_usage`);
        const data = await response.json();

        document.getElementById("current-usage").value = data.current_usage;
        document.getElementById("remaining-budget").innerText = `Remaining Budget: ${data.remaining_budget} kWh`;
        document.getElementById("monthly-limit").value = data.monthly_limit;
        document.getElementById("ai-recommendation").innerText = data.recommendation;

        updateApplianceList(data.appliances);
    } catch (error) {
        console.error("Error fetching energy usage:", error);
    }
}

// Update monthly limit
async function updateLimit() {
    const newLimit = parseFloat(document.getElementById("monthly-limit").value);

    if (isNaN(newLimit) || newLimit <= 0) {
        alert("Please enter a valid monthly limit.");
        return;
    }

    try {
        await fetch(`${API_BASE_URL}/set_limit`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ monthly_limit: newLimit })
        });

        trackUsage();
    } catch (error) {
        console.error("Error updating monthly limit:", error);
    }
}

// Toggle appliance ON/OFF
async function toggleAppliance(state) {
    const appliance = document.getElementById("appliance").value;
    if (!appliance) {
        alert("Please select an appliance.");
        return;
    }

    try {
        await fetch(`${API_BASE_URL}/toggle_appliance`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ appliance: appliance, status: state })
        });

        document.getElementById("appliance-status").innerText = `${appliance} turned ${state}`;
        trackUsage();
    } catch (error) {
        console.error("Error toggling appliance:", error);
    }
}

// Update appliance list with remaining usage hours
function updateApplianceList(appliances) {
    const applianceList = document.getElementById("appliance-list");
    applianceList.innerHTML = "";

    appliances.forEach(appliance => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${appliance.name}</strong> - Power: ${appliance.usage} kW, 
                        Status: ${appliance.status}, Can run for: ${appliance.remaining_hours} hrs`;
        applianceList.appendChild(li);
    });
}

document.addEventListener("DOMContentLoaded", trackUsage);
