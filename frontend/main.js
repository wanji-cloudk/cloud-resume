window.addEventListener('DOMContentLoaded', () => {
    getVisitorCount();
});

// We will update this string placeholder after running our Terraform code
const apiEndpoint = "https://h0mgq2wpq5.execute-api.us-east-1.amazonaws.com/visitor";

function getVisitorCount() {
    fetch(apiEndpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not stable");
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('counter').innerText = data.count;
        })
        .catch(error => {
            console.error("Error fetching visitor counter:", error);
            document.getElementById('counter').innerText = "Err";
        });
}