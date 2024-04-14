// Listen to browser action icon click events
chrome.action.onClicked.addListener(function(tab) {
    const url = tab.url;
    // Set the backend API URL
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
        // Determine whether to display a warning based on the data returned by the backend service
        // It is assumed here that the data structure returned by the backend is {isPhishing: true/false}
        if(data.isPhishing) {
          alert('Warning: This is a Phishing Site!');
        } else {
          alert('This site is safe.');
        }
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Can not make phishing detection.');
    });
  });
  
  // Listen for extension installation and update events
  chrome.runtime.onInstalled.addListener(function (details) {
    if (details.reason == 'install') {
      console.log('Installed successfully');
    } else if (details.reason == "update") {
      var thisVersion = chrome.runtime.getManifest().version;
      console.log("Updated from " + details.previousVersion + " to " + thisVersion + "!");
    }
  });
