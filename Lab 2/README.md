SQL Injection: Login Bypass Lab

This repository contains a Python script to exploit a SQL Injection vulnerability in the login functionality of a web application. The goal of this lab is to demonstrate how an attacker can bypass authentication and log in as an administrator using SQL injection.
Lab Description

In this lab, the web application has a SQL injection vulnerability in the login function. The challenge is to exploit this vulnerability to log in as the administrator user without knowing the correct password.

To solve the lab, you will need to perform a SQL injection attack on the login form. The provided Python script demonstrates how to inject a payload to bypass the authentication mechanism.
Payload Used

The payload used in this lab is:

"administrator'--"

This payload comments out the rest of the SQL query, effectively logging the attacker in as the administrator user.
How to Use

    Clone the repository to your local machine.
    Install the required dependencies:

pip install requests beautifulsoup4

Run the script with the target URL and SQL injection payload:

python lab2.py <TARGET_URL> "<SQL_PAYLOAD>"

Example:

    python lab2.py https://0a0600be04a2058c803bc7d60022004f.web-security-academy.net/login "administrator'--"

The script will attempt to bypass the login and log you in as the administrator user.
Lab URL

This lab is part of the SQL Injection Learning Path provided by PortSwigger. You can access the lab at the following URL:
Login Bypass Lab - PortSwigger
Disclaimer

This repository is for educational purposes only. The scripts and challenges provided here should not be used on systems you do not own or have explicit permission to test.
Acknowledgments

Special thanks to PortSwigger for providing the SQL Injection Learning Path, which serves as the foundation for this lab.
