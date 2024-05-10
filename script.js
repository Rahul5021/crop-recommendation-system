document.getElementById("cropForm").addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById("cropForm"));
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });
    fetch("http://127.0.0.1:5000/predict", {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `<p>Recomendded crop: ${data.prediction}</p>`;
        })
        .catch(error => {
            console.log('Error:', error);
        });
});