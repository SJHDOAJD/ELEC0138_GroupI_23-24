document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('checkPage');
    checkPageButton.addEventListener('click', function() {
        
        // Get the URL of the current tab
        chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
            let url = tabs[0].url;
            // Send a request to the backend for detection
            fetch('http://localhost:5000/detect', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({url: url}),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Update results based on data returned by the backend service
                const resultElement = document.getElementById('result');
                if(data.isPhishing) {
                    resultElement.innerHTML = '<p style="color: red;">Warning: This is a Phishing Site!</p>';
                } else {
                    resultElement.innerHTML = '<p style="color: green;">This site is safe.</p>';
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                document.getElementById('result').textContent = 'Can not make phishing detection.';
            });
        });
        
    }, false);
}, false);
