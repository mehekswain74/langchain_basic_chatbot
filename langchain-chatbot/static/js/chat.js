function sendMessage() {
    var query = document.getElementById('query').value;
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({query: query}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('response').innerText = 'Error: ' + error;
    });
}

