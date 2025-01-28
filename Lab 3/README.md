# SQL Injection Lab: Determine the Number of Columns

## Lab Description
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. 

The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

## Script Functionality
The script automates the process of determining the number of columns returned by the query using the following steps:
1. Sends a series of SQL injection payloads with `ORDER BY` clauses to the vulnerable endpoint.
2. Monitors the application's response for an error (e.g., "Internal Server Error").
3. Identifies the number of columns by detecting the highest `ORDER BY` value that does not trigger an error.

If the injection is successful, the script outputs the number of columns. Otherwise, it indicates that the SQL injection attempt failed.

## Pre-requisites
1. **Vulnerable Application**: Access to the lab or a similar environment with a SQL injection vulnerability.
2. **Proxy Setup**: A proxy tool like Burp Suite to monitor and debug requests.
3. **Python Environment**: Python 3.x installed on your system.

## Requirements
1. **Python Libraries**:
   - `requests`: For sending HTTP requests.
   - `urllib3`: For handling SSL warnings.
2. **Proxy Configuration**:
   - The script uses a proxy at `http://127.0.0.1:8080`. Ensure your proxy tool (e.g., Burp Suite) is running and configured correctly.
3. **Command-line Arguments**:
   - The target URL must be passed as a command-line argument when running the script.

## Usage
1. Clone the repository or download the script to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install requests

## Run the script from the terminal:
python script_name.py <target_url>

## Lab URL
[SQL Injection: Determine the Number of Columns](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)
