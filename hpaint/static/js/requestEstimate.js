// version 1

// next version inorporate removing the form entirely by grabbing a 
// cookie the server sends saying you have done an estimate

document.addEventListener("DOMContentLoaded", function () {

    function submitRequestForm() {
        const nameVal = document.getElementById("name").value;
        const telephoneVal = document.getElementById("telephone").value;
        const emailVal = document.getElementById("email").value;
        const descriptionVal = document.getElementById("description").value;

        const formData = {
            name: nameVal,
            telephone: telephoneVal,
            email: emailVal,
            description: descriptionVal,
        };

        fetch("/request-estimate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Request failed");
            }
        })
        .then((data) => {
            console.log("Server response: ", data);
            // if the server sends a good response, clear the form
            clearForm();  
        })
        .catch((error) => {
            console.error("Error:", error);
            console.log("Response Status:", error.response.status);
            console.log("Response Text:", error.response.text());
        })

    }

    function clearForm() {
        // access specific input elements by their IDs and clear their values
        document.getElementById("telephone").value = "";
        document.getElementById("email").value = "";
        document.getElementById("description").value = "";
    }

    const requestEstimateForm = document.getElementById("request_estimate")
    requestEstimateForm.addEventListener("submit", function (e) {
        e.preventDefault();
        submitRequestForm();
    });
});
