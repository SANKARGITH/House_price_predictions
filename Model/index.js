async function loadLocations() {
    try {
        const response = await fetch("http://127.0.0.1:5000/locations");
        const data = await response.json();
        console.log("Fetched locations data:", data); // Log the entire response

        const locationSelect = document.getElementById("location");
        if (data && data.locations && Array.isArray(data.locations)) {
            data.locations.forEach(location => {
                if (typeof location === "string" && location.trim().length > 0) {
                    const option = document.createElement("option");
                    option.value = location;
                    option.textContent = location;
                    locationSelect.appendChild(option);
                }
            });
        } else {
            alert("No locations found. Please check the server response format.");
            console.error("Invalid locations data:", data);
        }
    } catch (error) {
        alert("Error fetching locations. Please check the server.");
        console.error("Error:", error);
    }
}

async function predictPrice() {
    const location = document.getElementById("location").value;
    const total_sqft = document.getElementById("total_sqft").value;
    const bath = document.getElementById("bath").value;
    const bhk = document.getElementById("bhk").value;

    const formData = new FormData();
    formData.append("location", location);
    formData.append("total_sqft", total_sqft);
    formData.append("bath", bath);
    formData.append("bhk", bhk);

    try {
        const response = await fetch("http://127.0.0.1:5000/get_predict_price", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `<h4>Estimated Price: ₹${data.predicted_price}L</h4>`;
    } catch (error) {
        alert("Error predicting price.Please Enter the Values");
        console.error("Error:", error);
    }
}

window.onload = loadLocations;
