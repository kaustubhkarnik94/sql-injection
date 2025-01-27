SQL Injection Lab - Login Function

This repository contains a Python script that demonstrates how to exploit a SQL injection vulnerability in a login function. The lab is based on the PortSwigger Web Security Academy, and the goal is to log in as the administrator user using a SQL injection attack.
Lab Description

This lab contains a SQL injection vulnerability in the login function of a web application. The objective is to exploit this vulnerability to bypass the login and gain access as the administrator user.

To solve the lab, you need to perform a SQL injection attack that manipulates the login request and successfully logs in as the administrator. The payload used for this attack is a SQL injection string that bypasses authentication.
Vulnerability Details

    Vulnerability: SQL Injection in the login function.
    Goal: Log in as the administrator user by exploiting the SQL injection vulnerability.

Script Overview

The provided script automates the process of exploiting the SQL injection vulnerability in the login form. It performs the following tasks:

    Fetches the CSRF Token: The script retrieves the CSRF token from the login page to ensure the request is valid.
    Exploits SQL Injection: The script sends a specially crafted SQL injection payload to the login form.
    Checks for Successful Login: The script checks if the login was successful by looking for the "Log out" text, which indicates that the user is logged in.

Prerequisites

    Python 3.x
    requests library
    BeautifulSoup from bs4 for parsing HTML
    A proxy tool like Burp Suite (optional, for intercepting and debugging traffic)

How to Use the Script

    Clone the Repository:

git clone <repository_url>
cd <repository_folder>

Install Dependencies: Ensure you have the required libraries installed:

pip install requests beautifulsoup4

Run the Script: To run the script, use the following command:

python lab2.py <url> "<payload>"

Replace <url> with the target URL of the login page and <payload> with the SQL injection payload. For example:

    python lab2.py https://0a0600be04a2058c803bc7d60022004f.web-security-academy.net/login "administrator'--"

    The script will attempt to log in using the provided SQL injection payload and will print whether the attack was successful.

How the Script Works

    Fetching CSRF Token:
    The script first fetches the CSRF token from the login page by sending a GET request. It uses BeautifulSoup to parse the HTML and extract the token.

    SQL Injection Payload:
    The script sends the payload ("administrator'--") as the username. This payload is designed to bypass the authentication mechanism and log in as the administrator. The password is set to a random string as the SQL injection bypasses the password check.

    Post Request:
    The script sends a POST request with the CSRF token, the SQL injection payload, and the password. If the login is successful, the response will contain the text "Log out", indicating that the attack was successful.

Disclaimer

This script is intended for educational purposes only. It demonstrates how to exploit SQL injection vulnerabilities in a controlled, ethical environment. Do not use this script on systems you do not own or have explicit permission to test.

The lab and vulnerability used in this script are part of the PortSwigger Web Security Academy. We thank PortSwigger for providing the learning materials and labs.

For more details on the lab, visit the official lab page:
https://portswigger.net/web-security/sql-injection/lab-login-bypass


Acknowledgments

Special thanks to PortSwigger for providing the SQL Injection learning path and the associated labs. These resources have been invaluable for understanding and practicing web application security.
