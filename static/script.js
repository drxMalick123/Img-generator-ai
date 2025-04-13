// function generateImage() {
//     let textInput = document.getElementById("textInput").value;
//     let outputDiv = document.getElementById("output");

//     fetch("http://127.0.0.1:5000/generate", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ text: textInput })
//     })
//     .then(response => response.json())
//     .then(data => {
//         outputDiv.innerHTML = `<img src="${data.image_url}" alt="Generated Image">`;
//     })
//     .catch(error => console.error("Error:", error));
// }

function generateImage() {
    console.log("Button clicked"); // Debugging log
    let textInput = document.getElementById("textInput").value;
    let outputDiv = document.getElementById("output");

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: textInput })
    })
    .then(response => response.json())
    .then(data => {
        outputDiv.innerHTML = `<img src="${data.image_url}" alt="Generated Image">`;
    })
    .catch(error => console.error("Error:", error));
}
