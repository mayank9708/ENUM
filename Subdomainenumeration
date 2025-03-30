import requests
import threading

domain = input("Enter the target domain (e.g., youtube.com): ").strip()
filename = input("Enter the subdomain wordlist file name (e.g., subdomain.txt): ").strip()

try:
    with open(filename) as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()

discovered_subdomains = []
lock = threading.Lock()

def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        response = requests.get(url, timeout=3)
    except requests.ConnectionError:
        return
    else:
        print("[+] Discovered Subdomain:", url)
        with lock:
            discovered_subdomains.append(url)

threads = []
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

output_filename = "discovered_subdomains.txt"
with open(output_filename, 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

print(f"\n[✔] Scan Complete. Results saved in '{output_filename}'.")
