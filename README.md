# QueryCaptor
NetQuerySniffer is a powerful network analysis tool designed to monitor and capture HTTP and DNS traffic in real-time. This tool allows users to intercept network packets and extract valuable search queries and domain requests made by devices connected to the same network.

Installation Instructions for QueryCaptor
For Windows:
Install Python:

Download and install Python from the official website: python.org.
During installation, ensure to check the box that says "Add Python to PATH".
Clone the Repository:

Open Command Prompt and run:
bash
Copier le code
git clone https://github.com/Mr-Najm-Ouchen/QueryCaptor.git
Navigate to the Directory:

Change into the cloned directory:
bash
Copier le code
cd QueryCaptor
Install Required Libraries:

Install the necessary libraries using pip:
bash
Copier le code
pip install scapy
Run the Tool:

Execute the script:
bash
Copier le code
python QueryCaptor.py
For macOS:
Install Python:

Python usually comes pre-installed on macOS. You can check by running:
bash
Copier le code
python3 --version
If it's not installed, download it from python.org.
Install Homebrew (if not installed):

Open Terminal and install Homebrew (if you don’t have it already):
bash
Copier le code
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Git:

Install Git using Homebrew:
bash
Copier le code
brew install git
Clone the Repository:

Clone the repository:
bash
Copier le code
git clone https://github.com/Mr-Najm-Ouchen/QueryCaptor.git
Navigate to the Directory:

Change into the cloned directory:
bash
Copier le code
cd QueryCaptor
Install Required Libraries:

Install the necessary libraries using pip:
bash
Copier le code
pip3 install scapy
Run the Tool:

Execute the script:
bash
Copier le code
python3 QueryCaptor.py
For Linux:
Install Python:

Most Linux distributions come with Python pre-installed. To check, run:
bash
Copier le code
python3 --version
If not installed, use your package manager to install it (e.g., sudo apt install python3 for Ubuntu).
Install Git:

If Git is not installed, you can install it via your package manager:
bash
Copier le code
sudo apt install git
Clone the Repository:

Open a terminal and run:
bash
Copier le code
git clone https://github.com/Mr-Najm-Ouchen/QueryCaptor.git
Navigate to the Directory:

Change into the cloned directory:
bash
Copier le code
cd QueryCaptor
Install Required Libraries:

Install the necessary libraries using pip:
bash
Copier le code
pip3 install scapy
Run the Tool:

Execute the script (make sure to use sudo if necessary):
bash
Copier le code
sudo python3 QueryCaptor.py
Usage Instructions
Starting the Tool:

Simply run the command provided above for your respective OS. The tool will begin listening for network packets.
Interpreting Output:

The console will display detected DNS requests and HTTP requests. For each detected request, it will show the domain being accessed and any search queries identified.
Important Note
Run with Administrator Privileges: On Windows, macOS, and Linux, ensure to run the terminal or command prompt as an administrator to allow the tool to capture packets.

Legal Disclaimer: Use this tool responsibly and only on networks where you have permission to monitor traffic. Unauthorized network monitoring is illegal and unethical.
