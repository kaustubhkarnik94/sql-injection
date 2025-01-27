# SQL Injection Script for PortSwigger Lab 1

## Lab 1: SQL Injection in Product Category Filter

## Lab URL
This lab is part of PortSwigger Web Security Academy. You can find the lab details and challenges at the following link:  
[SQL Injection Lab - Retrieve Hidden Data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

### Description
This lab demonstrates a SQL injection vulnerability in the product category filter. The application executes a SQL query similar to the following when a user selects a category:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1;
```

To solve the lab, the goal is to perform a SQL injection attack that reveals unreleased products by modifying the query logic.

### Script Details
The provided Python script performs a SQL injection attack by sending a crafted payload in the category filter parameter.

### Features
- Sends a GET request to the target URL with the SQL injection payload.
- Checks the response for success indicators (e.g., the word "Congratulations").
- Prints debugging information, including the status code and the first 200 characters of the response body.

### Usage
```bash
python lab1.py <url> <payload>
```

#### Example
```bash
python lab1.py https://example.com "' OR 1=1 --"
```

### Code Workflow
1. Disables SSL warnings for cleaner output.
2. Configures a proxy for debugging purposes (default: Burp Suite at `127.0.0.1:8080`).
3. Sends a GET request with the payload appended to the category filter endpoint.
4. Analyzes the response for a success indicator ("Congratulations").
5. Prints whether the SQL injection was successful or not.

### Example Payload
The following payload bypasses the query filter and reveals unreleased products:

```sql
' OR 1=1 --
```

---

## Prerequisites
- Python 3.x
- Required libraries:
  - `requests`
  - `urllib3`

Install dependencies using:
```bash
pip install -r requirements.txt
```

### Requirements File (`requirements.txt`)
```
requests
urllib3
```

---

## Debugging Tips
- Use Burp Suite or a similar proxy tool to inspect requests and responses.
- Ensure the target URL is correct and accessible.
- Use `print` statements or logging for additional insights during script execution.

---

## Disclaimer
This script is for educational purposes only. It is owned by PortSwigger, and we thank them for providing the labs. Do not use this script on systems you do not own or have explicit permission to test.


