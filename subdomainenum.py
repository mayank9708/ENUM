import requests
import threading

domain = 'youtube.com'

with open('subdomain.txt') as file:
	subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock()

def check_subdoamin(subdomain):

	url = f'http://{subdomain}.{domain}'
	try:
		request.get(url)
	except requests.ConnectionError:
		pass
	else:
		print("[+] Discovered Subdomain: ", url)
		with lock:
			discovered_subdomains.append(url)

threads = []

for subdomain in subdomains:
	thread = threading.Thread(target=check_subdomain, args=(subdomains,))
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

with open("discovered_subdomains.txt", 'w') as f:
	for subdomain in discovered_subdomains:
		print(subdomain, file=f)
