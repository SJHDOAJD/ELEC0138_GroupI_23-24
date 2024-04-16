# Security and Privacy 23-24

# UCL ELEC0138 Final Assignment by TEAM I

# Before you start using the code, you must look at the following 'Usage' section ！！！！

## The presentation video 

- Link: https://www.youtube.com/watch?v=foXyj5P7JNk
- Since the video is non-public, You can only find it through the URL.

## Group Member

- 23037969
- 20087746
- 23038138
- 23083978

## Description

- This coursework aims to explore the complexities of securing smart home environments, with a particular focus on smart IOT devices. Since our environment is smart home and the main object is the camera, we mainly consider the threats posed by hackers. Based on this, we choose the two most classical attacks, which are DDoS and phishing attack. DDoS attacks the whole system. Phishing attack steals information by targeting the victim. Two defence systems have been created to deal with these two attacks separately.

## Content

- PhishingAttack: This folder contains code about phishing attack and designed phishing site.
- PhishingDefence: This folder contains backend program, post-training model, plug-in (defence) folder and model's training history.
- DDoS Attack: This floder contains the DDoS attack data, and the detection training model.
- DDoS Defence: This folder contains the DDoS detection code, DDoS defense code, the simulate html interface, and the test data.

## Point

- DDoS Attack: This attack is created using kali's tools, includes "hping3" and "slowhttptest".

## Usage

### To use the Phishing Attack:
- Clone PhishingAttack folder to a local computer.
- Next step is very important !!!!!!
- Use 'ipconfig' in cmd terminal to find your IP Address. Then, follow the comment in setup.py to change host value to your IP address.
- Installing Python 3.11
- Run the setup.py. You will get phishing address on the terminal. 
- You can open the phishing address in your local environment or virtual (Kali) environment. And, make a test.
- You can find result on the terminal.
- The video also show a email attack through kali tool.

### To use the DDoS Attack:
- Make sure that You have "hping3" and "slowhttptest" tools installed in Kali.
- The web server is setup using http.server (comes with python3 installation) on a Ubuntu VM, and run on the machine's IP address.
- SYN and UDP attacks are performed using "hping3", "Slowhttptest" for HTTP flooding attacks, using the web server address as the target.
- Tool parameters can be varied to change intensity/speed of attack.
- The results can be seen by wireshark pcap file, VM CPU load and web server.
- The code for the terminal run and some of the steps can be followed from our YouTube video.

### To use the Phishing Defence:
- Clone PhishingDefence folder to local computer.
- Turn on developer mode in Google's extensions and Load to unpack extension (defence folder). And, Pin the plugin to the toolbar.
- Run the setup.py. The backend program starts and you can interact with plug-in. The results would show below the plug-in button and on the terminal.

### To use the DDoS Defence:
- Installing Python 3.12.0 or above version.
- Run the "DDoS Detection Code.ipynb" file, and obtain the trained model: DNN_model.keras
- Run the file "ddos+defence.py" to create the DDoS detection server, and then run html file"testing+web.html" to upload the simulation data (DDOS1.csv, and DDOS2.csv) to test. 

## Packet required
To run the code, the following packages are required:
- `flask`
- `flask-cors`
- `joblib`
- `requests`
- `numpy`
- `pandas`
- `matplotlib`
- `missingno`
- `sklearn.preprocessing`
- `sklearn.impute`
- `werkzeug.utils`
- `xgboost`
- `tensorflow`
- `os`
- `tqdm`
- `gc`
- `sklearn`
- `seaborn`

To make DDoS Attack, the following tools are required:
- `hping3`
- `slowhttptest`
- `python3` on target VM