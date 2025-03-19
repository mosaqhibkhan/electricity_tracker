// const API_BASE_URL = "http://127.0.0.1:5000"; // Flask server URL

// // Fetch and display energy usage
// async function trackUsage() {
//     try {
//         const response = await fetch(`${API_BASE_URL}/get_usage`);
//         const data = await response.json();

//         document.getElementById("current-usage").value = data.current_usage;
//         document.getElementById("remaining-budget").innerText = `Remaining Budget: ${data.remaining_budget} kWh`;
//     } catch (error) {
//         console.error("Error fetching energy usage:", error);
//     }
// }

// // Toggle appliance ON/OFF
// async function toggleAppliance(action) {
//     const appliance = document.getElementById("appliance").value;

//     if (!appliance) {
//         alert("Please select an appliance!");
//         return;
//     }

//     try {
//         const response = await fetch(`${API_BASE_URL}/toggle_appliance`, {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ appliance, action })
//         });

//         const result = await response.json();
//         document.getElementById("appliance-status").innerText = result.message || "Action completed";

//         // Fetch updated energy usage after toggling appliance
//         trackUsage();
//     } catch (error) {
//         console.error("Error toggling appliance:", error);
//     }
// }

// // Auto-fetch ESP32 data every 5 seconds
// setInterval(trackUsage, 5000);

// // Load data on page load
// document.addEventListener("DOMContentLoaded", trackUsage);


//end of first code


// const API_BASE_URL = "http://127.0.0.1:5000"; // Flask server URL

// // Fetch and display energy usage
// async function trackUsage() {
//     try {
//         const response = await fetch(`${API_BASE_URL}/get_usage`);
//         const data = await response.json();

//         document.getElementById("current-usage").value = data.current_usage; // Update input field
//         document.getElementById("remaining-budget").innerText = `Remaining Budget: ${data.remaining_budget} kWh`;
//     } catch (error) {
//         console.error("Error fetching energy usage:", error);
//     }
// }

// // Toggle appliance ON/OFF
// async function toggleAppliance(action) {
//     const appliance = document.getElementById("appliance").value;

//     if (!appliance) {
//         alert("Please select an appliance!");
//         return;
//     }

//     try {
//         const response = await fetch(`${API_BASE_URL}/toggle_appliance`, {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ appliance, action })
//         });

//         const result = await response.json();
//         document.getElementById("appliance-status").innerText = result.message || "Action completed";

//         // Fetch updated energy usage after toggling appliance
//         trackUsage();
//     } catch (error) {
//         console.error("Error toggling appliance:", error);
//     }
// }

// // Simulate ESP32 sending data (for testing)
// async function simulateEsp32Data() {
//     try {
//         await fetch(`${API_BASE_URL}/esp32_status`, {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ energy_consumed: 5 }) // Simulating +5 kWh consumption
//         });
//     } catch (error) {
//         console.error("Error sending ESP32 data:", error);
//     }
// }

// // Auto-fetch ESP32 data every 5 seconds
// setInterval(() => {
//     trackUsage();
//     simulateEsp32Data(); // Simulate ESP32 updates (REMOVE THIS when using real ESP32)
// }, 5000);

// // Load data on page load
// document.addEventListener("DOMContentLoaded", trackUsage);

//end of second code


// const API_BASE_URL = "http://127.0.0.1:5000"; // Flask server URL

// // Fetch and display energy usage
// async function trackUsage() {
//     try {
//         const response = await fetch(`${API_BASE_URL}/get_usage`);
//         const data = await response.json();

//         document.getElementById("current-usage").value = data.current_usage;
//         document.getElementById("remaining-budget").innerText = `Remaining Budget: ${data.remaining_budget} kWh`;

//         // Ensure the monthly limit field shows the correct value
//         document.getElementById("monthly-limit").value = data.monthly_limit;
//     } catch (error) {
//         console.error("Error fetching energy usage:", error);
//     }
// }

// // Update monthly limit when user inputs a value
// async function updateLimit() {
//     const newLimit = parseFloat(document.getElementById("monthly-limit").value);

//     if (isNaN(newLimit) || newLimit <= 0) {
//         alert("Please enter a valid monthly limit.");
//         return;
//     }

//     try {
//         const response = await fetch(`${API_BASE_URL}/set_limit`, {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ monthly_limit: newLimit })
//         });

//         const result = await response.json();
//         alert(result.message || "Monthly limit updated!");

//         trackUsage(); // Refresh UI after update
//     } catch (error) {
//         console.error("Error updating monthly limit:", error);
//     }
// }

// // Toggle appliance ON/OFF
// async function toggleAppliance(action) {
//     const appliance = document.getElementById("appliance").value;

//     if (!appliance) {
//         alert("Please select an appliance!");
//         return;
//     }

//     try {
//         const response = await fetch(`${API_BASE_URL}/toggle_appliance`, {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ appliance, action })
//         });

//         const result = await response.json();
//         document.getElementById("appliance-status").innerText = result.message || "Action completed";

//         // Fetch updated energy usage after toggling appliance
//         trackUsage();
//     } catch (error) {
//         console.error("Error toggling appliance:", error);
//     }
// }

// // Auto-fetch ESP32 data every 5 seconds
// setInterval(trackUsage, 5000);

// // Attach event listener to input field to update limit on change
// document.getElementById("monthly-limit").addEventListener("change", updateLimit);

// // Load data on page load
// document.addEventListener("DOMContentLoaded", trackUsage);

// End of third code

const API_BASE_URL = "http://127.0.0.1:5000"; // Flask server URL

// Fetch and display energy usage
async function trackUsage() {
    try {
        const response = await fetch(`${API_BASE_URL}/get_usage`);
        const data = await response.json();

        document.getElementById("current-usage").value = data.current_usage;
        document.getElementById("remaining-budget").innerText = `Remaining Budget: ${data.remaining_budget} kWh`;
        document.getElementById("monthly-limit").value = data.monthly_limit;

        updateApplianceList(data.appliances, data.remaining_budget);
    } catch (error) {
        console.error("Error fetching energy usage:", error);
    }
}

// Update monthly limit when user inputs a value
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

        trackUsage(); // Refresh UI
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

// Update appliance list with estimated usage
function updateApplianceList(appliances, remainingBudget) {
    const applianceList = document.getElementById("appliance-list");
    applianceList.innerHTML = "";

    appliances.forEach(appliance => {
        const remainingHours = (remainingBudget / appliance.usage).toFixed(2);
        const li = document.createElement("li");
        li.innerHTML = `<strong>${appliance.name}</strong> - Power: ${appliance.usage} kW, Can run for: ${remainingHours} hrs`;
        applianceList.appendChild(li);
    });
}

// Load data on page load
document.addEventListener("DOMContentLoaded", trackUsage);


